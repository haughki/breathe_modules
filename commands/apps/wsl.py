from commands.imports import *
from supporting import utils

Breathe.add_commands(
    context = AppContext(executable='ubuntu') | AppContext(executable='WindowsTerminal'),
    mapping = {
        "full-screen": Key("a-enter"),

        "new tab": Key("cs-t"),
        "(duplicate | dupe) tab": Key("cs-d"),
        "next tab [<t>]": Key("c-tab"),
        "(preev | previous) tab [<t>]": Key("cs-tab"),
        # "move tab right [<t>]": Key("cas-right/5:%(t)d"),
        # "move tab left [<t>]": Key("cas-left/5:%(t)d"),
        "close tab": Key("c-w"),

        # "show find": Key("cs-f"),
        "find <text>": Key("cs-f/25") + Text("%(text)s"),
        # "find next [<n>]": Key("f3:%(n)d"),
        # "find (prev | previous) [<n>]": Key("s-f3:%(n)d"),

        # directories
        "project[s]": Text("proj") + Key("enter"),
        "Windows temp": Text("dtemp") + Key("enter"),
        "hawk user": Text("hawk") + Key("enter"),
        "mount delta": Text("/mnt/d/"),
        "mount Charlie": Text("/mnt/c/"),

        # midnight commander
        "show find": ContextAction(
            default=None, actions=
            [
                (AppContext(executable="WindowsTerminal", title="mc ["), Key("c-s")),
                (AppContext(executable="WindowsTerminal"), Key("cs-f")),
            ],
        ),
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