from commands.imports import *
from supporting import utils
import time, logging, re
rule_log = logging.getLogger("rule")

"""
Tries to match windows using "focus" <app_name> [<title_fragment>]. The dict below correlates the spoken app_name key
with an (<exe name>, <window title hint>). The hint is hard-coded, whereas the title_fragment is dictation, dictation
which let's you choose, in real-time, between multiple windows with the same process name. If your app_name command
is the same as the exe_name, you can leave out the exe_name.

To see data about the current available windows (including the actual names to use here), try "print windows".
"""
window_map = {
    "breathe": {"exe_name": "idea64", "title_hint": "breathe_modules"},
    "code working": {"exe_name": "code", "title_hint": "working"},
    "code registration": {"exe_name": "code", "title_hint": "registration"},
    "note": {"exe_name": "notepad", "title_hint": "voice working"},
    # "note": {"exe_name": "natspeak", "title_hint": "voice working dragon"},
    "pad working": {"exe_name": "notepad", "title_hint": "pad working"},
    "daily tasks": {"exe_name": "wordpad", "title_hint": "daily tasks"},
    "questions": {"exe_name": "wordpad", "title_hint": "running questions"},
    "peptide": {"exe_name": "idea64", "title_hint": "peptide-webapp"},
    # "Dragon": {"exe_name": "idea64", "title_hint": "dragonfly-project"},
    # "Python library": {"exe_name": "idea64", "title_hint": "python-code-library"},
    # "Java library": {"exe_name": "idea64", "title_hint": "java-code-library"},

    "anki": {"exe_name": "anki", "title_hint": ""},
    "chrome": {"exe_name": "", "title_hint": "Google Chrome"},   # Special hack to exclude Workona hidden tabs window from focus
    "chat": {"exe_name": "chrome", "title_hint": "Chat"},
    "code": {"exe_name": "", "title_hint": ""},
    "command": {"exe_name": "cmd", "title_hint": "command prompt"},
    "dragonpad": {"exe_name": "natspeak", "title_hint": "dragonpad"},
    "evernote": {"exe_name": "evernote", "title_hint": "evernote"},
    "explore": {"exe_name": "explorer", "title_hint": ""},
    "idea": {"exe_name": "", "title_hint": ""},
    "Indeni": {"exe_name": "virtualbox", "title_hint": "indeni server"},
    "mobile": {"exe_name": "mobaxterm", "title_hint": ""},
    "NatLink": {"exe_name": "natspeak", "title_hint": "messages from Natlink"},
    "Notepad": {"exe_name": "notepad", "title_hint": "Notepad"},
    "word pad": {"exe_name": "wordpad", "title_hint": ""},
    "slack": {"exe_name": "", "title_hint": ""},
    "snag it": {"exe_name": "SnagitEditor", "title_hint": ""},
    "task manager": {"exe_name": "taskmgr", "title_hint": "Windows Task Manager"},
    "ooboo": {"exe_name": "ubuntu", "title_hint": ""},
    "Ubuntu": {"exe_name": "ubuntu", "title_hint": ""},
    "virtual": {"exe_name": "virtualbox", "title_hint": "ubuntu-desktop"},
    "term": {"exe_name": "WindowsTerminal", "title_hint": ""},
    "Windows get": {"exe_name": "mintty", "title_hint": ""},
    "word": {"exe_name": "winword", "title_hint": ""},
}

config = Config("Window control")
config.lang                = Section("Language section")
config.lang.focus_win      = Item("focus <win_selector>",
                                  doc="Bring a named window to the foreground. 'focus chrome'")
config.lang.transfer_win   = Item("transfer <win_selector>",
                                  doc="Copy all of the text in the current window, focus the target window, And paste. 'transfer anki'")
config.lang.focus_title    = Item("focus title <text>",
                                  doc="Bring a window with a given title (or title fraction) to the foreground. 'focus chrome google maps'")
config.lang.place_win      = Item("place <win_selector> (<position> [on <mon_selector>] | on <mon_selector>)",
                                  doc="Move a window to a monitor or to a location on a monitor. 'place chrome on 2' or 'place chrome top on 2'")
config.lang.nudge_win      = Item("nudge <win_selector> <direction> [<nudge_multiplier>]",
                                  doc="Nudge a window in a direction. 'nudge chrome right 6'")
config.lang.resize_win     = Item("resize <win_selector> [from] <position> [to] <position> [on <mon_selector>]",
                                  doc="Move and resize a window. 'resize chrome top right on 2'")
config.lang.stretch_win    = Item("stretch <win_selector> [to] <position>",
                                  doc="Stretch a window in a direction. 'stretch chrome left'")
config.lang.place_win_fraction = Item("place <win_selector> <position> <screen_fraction>",
                                      doc="Place a window according to a screen fraction. 'place chrome top third'")

config.lang.win_selector   = Item("[(this | current | window)] | <win_names> [<title_fragment>]",
                                  doc="Partial command for specifying a window; must contain the <win_names> extra.")
config.lang.mon_selector   = Item("(this | current) monitor | [monitor] <mon_names>",
                                  doc="Partial command for specifying a monitor; must contain the <mon_names> extra.")
config.lang.left           = Item("left", doc="Word for direction left or left side of monitor.")
config.lang.right          = Item("right", doc="Word for direction right or right side of monitor.")
config.lang.up             = Item("up", doc="Word for direction up.")
config.lang.down           = Item("down", doc="Word for direction down.")
config.lang.top            = Item("top", doc="Word for top side of monitor.")
config.lang.bottom         = Item("bottom", doc="Word for bottom side of monitor.")
config.lang.screen_fractions = Item({
    "half":     0.5,
    "third":    0.33,
    "quarter":  0.25,
},
    doc="Fractions of the screen")

config.settings            = Section("Settings section")
config.settings.grid       = Item(10, doc="The number of grid divisions a monitor is divided up into when placing windows.")
config.load()



""" Window Selection """

# Build the list of common window names
win_names     = DictList("win_names")
win_names_ref = DictListRef("win_names", win_names)
for key in window_map.keys():
    win_names[key] = key

# Helper function to search for a default-name window.
def get_app_window(app_name, title_fragment=None):
    if title_fragment:
        title_fragment = title_fragment.lower()
    return find_window(app_name, title_fragment, **window_map[app_name])  # The last parameter here unpacks the dictionary into named parameters based on the dictionary keys.

def find_window(app_name, title_fragment, exe_name, title_hint):
    # exe_name, title_hint = default_names[app_name]
    if not exe_name:
        exe_name = app_name
    exe_name = exe_name.lower()
    if title_hint:
        title_hint = title_hint.lower()

    best_match = None
    got_title_hint_match = False

    # print "exe: " + exe_name
    # print "title frag: " + title_fragment
    # print "title hint: " + title_hint

    all_windows = Window.get_all_windows()
    # windows.sort(key=lambda x: x.executable
    for window in all_windows:
        if not utils.windowIsValid(window):
            continue

        rule_log.debug("wanted exe:{} actual exe:{}".format(exe_name.encode('utf-8'), window.executable.encode('utf-8').lower()))
        rule_log.debug("hint:{} title:{}".format(title_hint.encode('utf-8'), window.title.encode('utf-8').lower()))
        rule_log.debug("fragment:{} title:{}".format(title_fragment.encode('utf-8'), window.title.encode('utf-8').lower()))

        # there will always be an exe name because of check above
        if window.executable.lower().find(exe_name) != -1:
            if exe_name == "chrome" and re.search(r"hidden tab(s?)\s*-\s*workona", window.title.lower()):  #     window.title.lower().find("hidden tabs - workona") != -1:  # custom rule to never focus workona hidden tabs
                continue
            if not title_fragment and not title_hint:
                best_match = window
                break
            if not got_title_hint_match:
                best_match = window
            if title_fragment and window.title.lower().find(title_fragment) != -1:
                best_match = window
                break
            if title_hint and window.title.lower().find(title_hint) != -1:
                best_match = window
                got_title_hint_match = True

    if not best_match:
        raise StandardError(
            "Found no match for app_name: " + str(app_name) + " with title_fragment: " + str(title_fragment))

    # best_match.name = app_name
    return best_match


class WinSelectorRule(CompoundRule):

    spec = config.lang.win_selector
    #spec = "[(this | current | window)] | <win_names> [<title_fragment>]"
    extras = [
        win_names_ref,
        Dictation("title_fragment"),
    ]
    exported = False

    def value(self, node):
        if node.has_child_with_name("win_names"):
            app_name = node.get_child_by_name("win_names").value()
            # print "app_name: " + str(app_name)
            title_fragment = ""
            if node.has_child_with_name("title_fragment"):
                title_fragment = str(node.get_child_by_name("title_fragment").value())
                # print "title_fragment: " + title_fragment
            return get_app_window(app_name, title_fragment)
        return Window.get_foreground()


win_selector = RuleRef(WinSelectorRule(), name="win_selector")

""" Copy the contents of the current window to the target window. """
def transfer_win(win_selector=None):
    Key("c-a, c-c").execute()
    focus_win(win_selector)
    # Key("c-v").execute()

""" Focus a Window """
def focus_win(win_selector=None, app_name=None):
    if not win_selector and not app_name:
        rule_log.error("win_selector or app_name cannot both be empty.")
    if win_selector:
        window = win_selector
    else:
        window = get_app_window(app_name, "")
    if not window:
        rule_log.warning("No window with that name found.", exc_info=True)
        return
    #rule_log.debug("bringing window '%s' to the foreground." % window)
    for attempt in range(4):
        try:
            window.set_foreground()
        except Exception, e:
            rule_log.warning("set_foreground() failed: %s." % e, exc_info=True)
            time.sleep(0.2)
        else:
            break


""" Monitor Selection """

mon_names     = DictList("mon_names")
mon_names_ref = DictListRef("mon_names", mon_names)

# Populate monitor names.
for i, m in enumerate(monitors):
    mon_names[str(i+1)] = m

class MonSelectorRule(CompoundRule):
    spec = config.lang.mon_selector
    #spec = "(this | current) monitor | [monitor] <mon_names>"
    extras = [mon_names_ref]
    exported = False

    def value(self, node):
        if node.has_child_with_name("mon_names"):
            return node.get_child_by_name("mon_names").value()
        return None

mon_selector = RuleRef(MonSelectorRule(), name="mon_selector")


"""
It's unclear to me exactly how this grid thing works. I tried a variety of different commands to try and understand,
but I still don't quite get it. I never tried to use commands with the "grid", but I'm just going to leave it here for now
in case I want to try to do something with it later.
"""
class GridRule(Rule):
    sections = config.settings.grid
    def __init__(self):
        Rule.__init__(self,
                      name="grid",
                      element=Integer("_grid", 0, self.sections + 1),
                      exported=False)

    def value(self, node):
        value = node.get_child_by_name("_grid").value()
        return float(value) / self.sections

grid_rule = GridRule()


#---------------------------------------------------------------------------
""" Position """
horz_left    = Compound(config.lang.left,   name="horz", value=0.0)
horz_right   = Compound(config.lang.right,  name="horz", value=1.0)
vert_top     = Compound(config.lang.top,    name="vert", value=0.0)
vert_bottom  = Compound(config.lang.bottom, name="vert", value=1.0)
horz_grid    = RuleRef(grid_rule, name="horz")
vert_grid    = RuleRef(grid_rule, name="vert")

horz_expl    = Alternative([horz_left, horz_right],  name="horz_expl")
horz_all     = Alternative([horz_expl, horz_grid], name="horz_all")
vert_expl    = Alternative([vert_top,  vert_bottom], name="vert_expl")
vert_all     = Alternative([vert_expl, vert_grid], name="vert_all")

# I've added the commands in comments as I think they should be. They don't work as expected.
# I did some hacking on the place_win() function, and maybe that's why it doesn't work properly.
# But, at this point, I don't really use any of the position commands, so I'm not worried about it;
# just leaving it here for now in case I want to make it work at some point.
position_element = Compound(
    spec="   <horz_expl>"              # 1D, horizontal             (left | right)  OR
         " | <vert_expl>"              # 1D, vertical               (top | bottom)  OR
         " | <horz_all> <vert_all>"    # 2D, horizontal-vertical    ((left | right) | 1- 10) ((top | bottom) | 1-10)  OR
         " | <vert_expl> <horz_all>"   # 2D, vertical-horizontal    (top | bottom) ((left | right) | 1- 10)  OR
         " | <vert_all> <horz_expl>",  # 2D, vertical-horizontal    ((top | bottom) | 1-10) (left | right)
    extras=[horz_expl, horz_all, vert_expl, vert_all],
)
position_rule = Rule(
    name="position_rule",
    element=position_element,
    exported=False,
)
position = RuleRef(position_rule, name="position")


""" Place a Window On a Monitor """
def place_win(_node, win_selector, position=None, mon_selector=None):
    node = _node
    # Determine which window to place on which monitor.
    window = win_selector

    # "monitor" is the destination monitor.
    if mon_selector:
        monitor = mon_selector.rectangle
    else:
        monitor = window.get_containing_monitor().rectangle

    # Calculate available area within monitor.
    # x1, y1 is a (top?) left corner point. Not sure what the 1 is about.
    # dx, dy are dimensions of a rectangle.
    pos = window.get_position()       # Absolute position, across all monitors, of the window where it started before the move.
    m_x1 = monitor.x1 + pos.dx / 2    # The horizontal origin of the destination monitor, plus half the width of the original window.
    m_dx = monitor.dx - pos.dx        # The width of the destination monitor minus the width of the original window.
    m_y1 = monitor.y1 + pos.dy / 2
    m_dy = monitor.dy - pos.dy

    # Get spoken position and calculate how far to move.
    # A command can specify a horizontal and/or vertical destination (left/right, top/bottom) or not.
    # If it doesn't, specify a horizontal, calculate the destination horizontal to be the same as the
    # start horizontal; that is, the window should be in the same position it was on the starting
    # monitor. THIS ASSUMES THE SIZE OF ALL MONITORS IS EQUAL.
    horizontal = node.get_child_by_name("horz")
    # print "horizontal: " + str(horizontal)

    if horizontal:
        # print "pos.center.x: " + str(pos.center.x)
        dx = m_x1 + (horizontal.value() * m_dx) - pos.center.x
        # print "horizontal_value: " + str(horizontal.value())
    else:
        # THE FOLLOWING CODE ASSUMES THE SIZE OF ALL MONITORS IS EQUAL.
        # If I don't specify a horizontal destination (left/right), then I want to move the window to exactly the same horizontal
        # on the new monitor -- the same horizontal it had the old monitor. This is just what I wanted -- it seemed to make the
        # most sense to me, and I couldn't understand why the existing code was defaulting to moving the window to the left-hand
        # side of the screen, even when I didn't specify "left". It turns out there's a reason :-)
        #
        # At this point in the code, we know the absolute (across all monitors) x,y starting point and original dimensions of the
        # window we are moving. We also know the absolute x,y corner and dimensions of the monitor we are moving to. BUT, we don't
        # know anything about _which_ monitor we started on, nor do we know anything (dimensions, etc.) about that monitor.
        # Without this information, it seems to be impossible (?) to "robustly" calculate the destination horizontal we want. By
        # "robustly", I mean to calculate the horizontal for all possible combinations of monitors of different sizes. For example,
        # if monitor one was 800 x 600, and monitor two was 1920 x 1200 (or possibly vice versa, or three monitors, all of different
        # sizes, etc.), it doesn't seem possible to calculate the horizontal that I want; that is, the same horizontal as a window
        # had before the move.
        #
        # I think that's why the original author chose to default to left. I decided that since both my monitors are the same size,
        # that I would just assume that, and write the code that I wanted. If at some point I had a laptop into the mix here, I
        # should revert back to the old code which is simply: 'dx = m_x1 - pos.center.x' -- see commented out code at the bottom of
        # the code block.

        # print "pos.x1: " + str(pos.x1)
        start_monitor = 1  # leftmost monitor
        target_monitor = 1
        if pos.x1 >= monitor.dx:
            start_monitor = 2  # rightmost monitor

        if monitor.x1 > 0:
            target_monitor = 2

        # print "start_monitor: " + str(start_monitor)
        # print "target_monitor: " + str(target_monitor)

        dx = 0
        if start_monitor == 1 and target_monitor == 2:
            dx = monitor.dx
        elif start_monitor == 2 and target_monitor == 1:
            dx = -monitor.dx

        # This is the original code that 'hard codes'the destination horizontal to 'left'. See comments above.
        #dx = m_x1 - pos.center.x


    vertical = node.get_child_by_name("vert")
    # print "vertical: " + str(vertical)
    if vertical:
        dy = m_y1 + vertical.value() * m_dy - pos.center.y
    else:
        dy = 0

    # print "dx: " + str(dx)
    # print "dy: " + str(dy)

    # "Translate" and move window.
    # dx and dy represent the distance values to move the window from its current position to its new position.
    # So, for example, -10, 20 would move the window 10 pixels left and 20 pixels up.
    # print "*******"
    # print str(dx) + ", " + str(dy)
    pos.translate(dx, dy)
    # window.move(pos, animate="spline")
    window.move(pos)


""" Nudge """

nudge_increment = 20
direction_left    = Compound(config.lang.left,   name="direction_left", value=("x", -nudge_increment))
direction_right   = Compound(config.lang.right,  name="direction_right", value=("x", nudge_increment))
direction_up    = Compound(config.lang.up,    name="direction_up", value=("y", -nudge_increment))
direction_down  = Compound(config.lang.down, name="direction_down", value=("y", nudge_increment))

nudge_basic    = Alternative([direction_left, direction_right, direction_up, direction_down],  name="nudge_basic")

direction_up_left = Sequence([direction_up, direction_left])
direction_up_right = Sequence([direction_up, direction_right])
direction_down_left = Sequence([direction_down, direction_left])
direction_down_right = Sequence([direction_down, direction_right])
nudge_diagonal = Alternative([direction_up_left, direction_up_right, direction_down_left, direction_down_right], name="nudge_diagonal")

direction_element = Compound(
    spec="   <nudge_basic>"
         " | <nudge_diagonal>",
    extras=[nudge_basic, nudge_diagonal],
)
direction_rule = Rule(
    name="direction_rule",
    element=direction_element,
    exported=False,
)
direction = RuleRef(direction_rule, name="direction")

nudge_multiplier = IntegerRef("nudge_multiplier", 1, 20)

def calculateNewPosition(direction_and_value, multiplier):
    new_position = [0, 0]
    if type(direction_and_value) is list:   # E.g., "nudge down right" --> [('y', 20), ('x', 20)]
        for direct in direction_and_value:
            val = direct[1] * multiplier
            if direct[0] == "x":
                new_position[0] += val
            else:
                new_position[1] += val
    else:  # we have a tuple with just one set of coordinates. For example: "nudge up" --> ('y', -20)
        val = direction_and_value[1] * multiplier
        if direction_and_value[0] == "x":
            new_position[0] = val
        else:
            new_position[1] = val
    return tuple(new_position)


def nudge_win(win_selector, direction, nudge_multiplier):
    # Determine which window to place on which monitor.
    window = win_selector
    a_direction = direction
    multiplier = 1
    if nudge_multiplier:
        multiplier = nudge_multiplier

    pos = window.get_position()
    new_position = calculateNewPosition(a_direction, multiplier)
    pos.translate(new_position[0], new_position[1])
    window.move(pos)


#---------------------------------------------------------------------------
def resize_win(_node, win_selector):
    node = _node
    window = win_selector
    pos = window.get_position()
    monitor = window.get_containing_monitor().rectangle

    # Determine horizontal positioning.
    nodes = node.get_children_by_name("horz")
    horizontals = [(monitor.x1 + n.value() * monitor.dx) for n in nodes]
    if len(horizontals) == 1:
        horizontals.extend([pos.x1, pos.x2])
    elif len(horizontals) != 2:
        rule_log.error("resize_win: Internal error.", exc_info=True)
        return
    x1, x2 = min(horizontals), max(horizontals)

    # Determine vertical positioning.
    nodes = node.get_children_by_name("vert")
    verticals = [(monitor.y1 + n.value() * monitor.dy) for n in nodes]
    if len(verticals) == 1:
        verticals.extend([pos.y1, pos.y2])
    elif len(verticals) != 2:
        rule_log.error("resize_win: Internal error.", exc_info=True)
        return
    y1, y2 = min(verticals), max(verticals)

    # Move window.
    pos = Rectangle(x1, y1, x2-x1, y2-y1)
    window.move(pos)   # , animate="spline"


#---------------------------------------------------------------------------
def stretch_win(_node, win_selector):
    node = _node
    # Determine which window to place.
    window = win_selector
    pos = window.get_position()
    monitor = window.get_containing_monitor().rectangle

    # Determine horizontal positioning.
    horizontals = [pos.x1, pos.x2]
    child = node.get_child_by_name("horz")
    if child: horizontals.append(monitor.x1 + child.value() * monitor.dx)
    x1, x2 = min(horizontals), max(horizontals)

    # Determine vertical positioning.
    verticals = [pos.y1, pos.y2]
    child = node.get_child_by_name("vert")
    if child: verticals.append(monitor.y1 + child.value() * monitor.dy)
    y1, y2 = min(verticals), max(verticals)

    # Move window.
    pos = Rectangle(x1, y1, x2-x1, y2-y1)
    window.move(pos) # , animate="spline"


# ---------------------------------------------------------------------------
screen_fraction = Choice("screen_fraction", config.lang.screen_fractions)

def fraction_win(_node, win_selector, screen_fraction):
    node = _node
    # Determine which window to place.
    window = win_selector
    #pos = window.get_position()
    monitor = window.get_containing_monitor().rectangle

    # Determine screen fraction.
    fraction = screen_fraction

    # Determine horizontal positioning.
    child = node.get_child_by_name("horz")
    if child:
        dx = monitor.dx * fraction
        x1 = monitor.x1 + child.value() * (monitor.dx - dx)
    else:
        dx = monitor.dx
        x1 = monitor.x1

    # Determine vertical positioning.
    child = node.get_child_by_name("vert")
    if child:
        dy = monitor.dy * fraction
        y1 = monitor.y1 + child.value() * (monitor.dy - dy)
    else:
        dy = monitor.dy
        y1 = monitor.y1

    # Move window.
    pos = Rectangle(x1, y1, dx, dy)
    window.move(pos) # , animate="spline"


Breathe.add_commands(
    None,
    {
        "<app_name>": Function(focus_win),
        config.lang.focus_win: Function(focus_win),
        config.lang.transfer_win: Function(transfer_win),
        config.lang.place_win: Function(place_win),
        config.lang.nudge_win: Function(nudge_win),
        config.lang.resize_win: Function(resize_win),
        config.lang.stretch_win: Function(stretch_win),
        config.lang.place_win_fraction: Function(fraction_win)
    },
    extras = [
        # "focus" shortcuts for certain high usage applications
        Alternative((
            Literal("breathe"),
            Literal("code working"),
            Literal("code register"),
            Literal("note"),
            Literal("chrome")), "app_name"),
        win_selector,
        mon_selector,
        position,
        direction,
        nudge_multiplier,
        screen_fraction,
    ],
    defaults={
        "nudge_multiplier": 1,
    }
)
