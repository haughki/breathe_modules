from commands.imports import *
from supporting import utils

def build_context(mc, terminal_default):
    return ContextAction(
        default=None, actions=
        [
            (AppContext(executable="WindowsTerminal", title="mc ["), mc),
            (AppContext(executable="WindowsTerminal"), terminal_default),
        ],
    )

windows_home = "/mnt/c"

Breathe.add_commands(
    context = AppContext(executable='ubuntu') | AppContext(executable='WindowsTerminal'),
    mapping = {
        "full-screen": Key("a-enter"),

        "new tab": Key("cs-t"),
        "(duplicate | dupe) tab": Key("cs-d"),
        "next tab [<t>]": Key("c-tab:%(t)d"),
        "preev tab [<t>]": Key("cs-tab:%(t)d"),
        # "move tab right [<t>]": Key("cas-right/5:%(t)d"),
        # "move tab left [<t>]": Key("cas-left/5:%(t)d"),
        "close tab": Key("c-f4"),
        "new pane": Key("as-d"),
        "close pane": Key("cs-w"),

        # "show find": Key("cs-f"),
        # "find next [<n>]": Key("f3:%(n)d"),
        # "find (prev | previous) [<n>]": Key("s-f3:%(n)d"),

        # directories
        "win home": Text("winhome") + Key("enter"),
        "put win home": Text(windows_home),
        "win projects": Text("winproj") + Key("enter"),
        "put win projects": Text(windows_home + "/projects"),
        "win temp": Text("wintmp") + Key("enter"),
        "put win temp": Text(windows_home + "/temp"),
        # "win root chow": Text("/mnt/c/"),
        # "win root drum": Text("/mnt/d/"),

        # midnight commander
        "go command": Key("c-o"),
        "go commander": Key("c-o"),
        "show find": build_context(Key("c-s"), Key("cs-f")),
        "find <text>": build_context(Key("c-s/25") + Text("%(text)s"), Key("cs-f/25") + Text("%(text)s")),

        "code <text>": Text("code %(text)s"),
        "WSL view": Text("wslview "),
    },

    extras = [
        Integer("t", 1, 50),
        Dictation("text"),
        Dictation("text2"),
        IntegerRef("n", 1, 50000),
        Integer("w", 0, 10),
        Integer("x", 0, 10),
        Integer("y", 0, 10),
        Integer("z", 0, 10)
    ],
    defaults = {
        "t": 1,
        "text": "",
        "text2": ""
    }
)

"""
class fmanRule(MappingRule):
    mapping = {
        "copy": R(Key("f5")),
        "deselect": R(Key("c-d")),
        "edit": R(Key("f4")),
        "explorer": R(Key("f10")),
        # Set these yourself and add them to the Choice at the bottom
        # Requires the favourites plug-in
        "go <fav>": R(Key("c-0") + Pause("15") + Text("%(fav)s") + Key("enter")),
        "go see": R(Key("c-p") + Pause("15") + Text("c") + Key("enter")),
        "go to": R(Key("c-p")),
        "move": R(Key("f6")),
        "new file": R(Key("s-f4")),
        "new folder": R(Key("f7")),
        "open left": R(Key("c-left")),
        "open right": R(Key("c-right")),
        "properties": R(Key("a-enter")),
        "refresh": R(Key("c-r")),
        "rename": R(Key("s-f6")),
        "search": R(Key("cs-f")),
        "set favourite": R(Key("s-f")),
        "show favourites": R(Key("c-0")),
        "(show | hide) hidden": R(Key("c-dot")),
        "sort [by] name": R(Key("c-f1")),
        "sort [by] size": R(Key("c-f2")),
        "sort [by] (modified | date)": R(Key("c-f3")),
        "(stoosh | copy) path": R(Key("f11")),
        "terminal": R(Key("f9")),
        "command pallette": R(Key("cs-p")),
    }
    extras = [
        IntegerRefST("num", 1, 4),
        Choice("fav", {
            "example favourite": "ef",
        }),
    ]
    defaults = {
        "num": 1,
    }
"""