from commands.imports import *
from supporting import utils, character

# disabled -- see quote below
def select_jump(c1, c2=None, c3=None):
    # print(str(c1) + "    " + str(c2)  + "    " + str(c3))
    c1 = character.NAMED_CHARACTER_MAP[c1] if c1 else None
    c2 = character.NAMED_CHARACTER_MAP[c2] if c2 else None
    c3 = character.NAMED_CHARACTER_MAP[c3] if c3 else None
    # print(str(c1) + "    " + str(c2)  + "    " + str(c3))
    Key("c-semicolon").execute()
    if c1: Key(c1).execute()
    if c2: Key(c2).execute()
    if c3: Key(c3).execute()
    Key("shift:down").execute()

def getFile(text=None):
    open_get_file_dialog = Key("cas-n")
    if text:
        open_get_file_dialog.execute()
        file_name = str(text).lower()
        Text(file_name).execute()
    else:
        open_get_file_dialog.execute()

is_full_screen = False
def toggleFullScreen():
    global is_full_screen
    if is_full_screen:
        # Key("cs-f12").execute()    # "Enter Distraction Free Mode"
        Key("cas-x").execute()    # "hide all tool windows"
        Key("w-down").execute()    # Windows OS for "restore window" -- doing this because IntelliJ's full screen mode is broken -- doesn't properly restore window after full-screen mode
        is_full_screen = False
    else:
        Key("w-up").execute()      # Windows OS for "maximize window"
        # Key("cs-f12").execute()    # "Enter Distraction Free Mode"
        Key("cas-x").execute()    # "hide all tool windows"
        is_full_screen = True

Breathe.add_commands(
    context=AppContext(executable="idea64"),
    mapping = {
        # Code execution.
        "run app": Key("s-f10"),
        "debug app": Key("s-f9"),
        "re-run app": Key("c-f5"),
        "run this [app]": Key("cs-f10"),
        "run test": Key("cs-f10"),
        "stop running": Key("c-f2"),
        "[toggle] (breakpoint | break)": Key("c-f8"),
        "step [over]": Key("f8"),
        "step into": Key("f11"),
        "step out": Key("s-f8"),
        "(keep running | resume)": Key("f9"),

        # Window handling
        # "preev file": Key("c-tab"),
        "next tab [<t>]": Key("a-right/5:%(t)d"),
        "preev tab [<t>]": Key("a-left/5:%(t)d"),
        "move tab right [<t>]": Key("cas-right/25:%(t)d"),
        "move tab left [<t>]": Key("cas-left/25:%(t)d"),
        "make tab first": Key("cas-up/5:%(t)d"),
        "make tab last": Key("cas-down/5:%(t)d"),
        "close tab [<n>]": Key("c-w:%(n)d"),

        # note: you can focus the editor from anywhere by using 'fly' (escape)
        "(full-screen | full screen)": Function(toggleFullScreen),  # macro, combination of: "Toggle Full Screen Mode" and "Hide All Tool Windows"
        "(Hide | hide | hi) bottom": Key("s-escape"),  # "hide active tool window"
        "(Hide | hide | hi) side": Key("cas-c"),  # "hide side tool windows"
        "float [file] structure": Key("c-f12"),
        "(go to | show) sidebar": Key("a-1"),
        "(go to | show) structure": Key("a-7"),
        "(go to | show) hierarchy": Key("a-8"),
        "(go to | show) version control": Key("a-9"),

        # Code navigation.
        "get file [<text>]": Function(getFile),  # "Navigate > File..."
        "sidebar file": Key("cs-j/25, enter"),
        "create [new] file": Key("cas-d"),
        "go to class": Key("c-n"),
        "go to (declaration | definition)": Key("c-b"),
        "go to implementation": Key("ca-b"),
        "go to super": Key("c-u"),

        "quick definition": Key("cs-i"),
        "quick (documentation | docs)": Key("c-q"),
        "toggle (book | bookmark)": Key("f7"),
        "next (book | bookmark) [<n>]": Key("cs-o:%(n)d"),
        "(prev | previous) book [<n>]": Key("cs-p:%(n)d"),
        "expand": Key("c-npadd"),
        "collapse": Key("c-npsub"),

        # settings.
        "(go to | show) module settings": Key("f4"),
        "(go to | show) project settings": Key("cas-s"),
        "(go to | show) [Global] settings": Key("ca-s"),

        # Terminal.
        "run terminal": Key("a-f12"),

        # Search.
        "replace [<text>]": Key("c-r/25") + Text("%(text)s"),
        "replace all": Key("a-a"),
        "show find": Key("c-f"),
        "find <text>": Key("c-f/25") + Text("%(text)s"),
        "find next [<n>]": Key("f3:%(n)d"),
        "find (prev | previous) [<n>]": Key("s-f3:%(n)d"),
        "find [in | and] files": Key("cs-f"),
        "find usages": Key("a-f7"),

        # Code
        "show intentions": Key("a-enter"),
        "accept choice": Key("c-enter"),
        "implement method": Key("c-i"),
        "override method": Key("c-o"),
        "(correct | red light bulb)": Key("a-enter"),
        "show complete": Key("c-space"),
        "context complete": Key("cs-space"),
        "syntax complete": Key("cs-enter"),
        "gets complete": Key("space, equal, space/10, cs-space"),

        # Edit
        "jump": Key("c-semicolon"),
        "select jump <c1> [<c2>] [<c3>]": Function(select_jump),
        "select word jump": Key("ca-semicolon"),
        "(declaration | definition) jump": Key("ctrl:down, semicolon, semicolon, ctrl:up"),
        # "line jump": Key("cs-semicolon"),

        "[shoreline | show] line <w> [<x>] [<y>] [<z>]": Key("c-g/50") + Function(utils.printNumber)+ Key("enter"),
        "comment [line | that | it]": Key("c-slash"),
        "show white space": Key("cs-w"),
        "redo": Key("cs-z"),
        "move line up [<n>]": Key("c-up:%(n)d"),
        "move line down [<n>]": Key("c-down:%(n)d"),

        # Version control
        "show diff": Key("c-d"),
        "next (diff | if) [<n>]": Key("f3:%(n)d"),
        "preev diff [<n>]": Key("s-f3:%(n)d"),
        "(get | git) pull": Key("c-t"),
        "(get | git) push": Key("cs-k"),
        "(get | git) commit": Key("c-k"),

        # Refactoring
        "(refactor|re-factor) (this|choose)": Key("cas-t"),
        "[(refactor|re-factor)] rename": Key("s-f6"),
        "[(refactor|re-factor)] change signature": Key("c-f6"),
        "(refactor|re-factor) move": Key("f6"),
        "(refactor|re-factor) copy": Key("f5"),
        "[(refactor|re-factor)] safe delete": Key("a-del"),
        "[(refactor|re-factor)] extract constant": Key("ca-c"),
        "[(refactor|re-factor)] extract field": Key("ca-f"),
        "[(refactor|re-factor)] extract parameter": Key("ca-p"),
        "[(refactor|re-factor)] extract variable": Key("ca-v"),
        "[(refactor|re-factor)] extract method": Key("ca-w"),
        "[(refactor|re-factor)] (in line|inline)": Key("ca-n"),

        # Custom key mappings.
        # "(run SSH session|run SSH console|run remote terminal|run remote console)": Key("a-f11/25, enter"),
    },
    extras = [
        Integer("t", 1, 50),
        Dictation("text"),
        IntegerRef("n", 1, 50000, default=1),
        Integer("w", 0, 10),
        Integer("x", 0, 10),
        Integer("y", 0, 10),
        Integer("z", 0, 10),
        Alternative(character.character_alternatives, name="c1"),
        Alternative(character.character_alternatives, name="c2"),
        Alternative(character.character_alternatives, name="c3"),
    ],
    defaults = {
        "t": 1,
    }
)