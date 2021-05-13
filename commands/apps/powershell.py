from commands.imports import *
from supporting import utils

# windows_home = "/mnt/c/Users/parkeh1"

# def build_context(mc, terminal_default):
#     return ContextAction(
#         default=None, actions=
#         [
#             (AppContext(executable="WindowsTerminal", title="mc ["), mc),
#             (AppContext(executable="WindowsTerminal"), terminal_default),
#         ],
#     )

Breathe.add_commands(
    context = AppContext(executable="WindowsTerminal", title="PowerShell"),
    mapping = {
        # directories
        # "projects": Text("cd ~\projects") + Key("enter"),
        # "temp directory": Text("cd ~\temp") + Key("enter"),

        # "put win home": Text(windows_home),
        # "win projects": Text("winproj") + Key("enter"),
        # "put win projects": Text(windows_home + "/projects"),
        # "win temp": Text("wintmp") + Key("enter"),
        # "put win temp": Text(windows_home + "/temp"),
        # "win root chow": Text("/mnt/c/"),
        # "win root drum": Text("/mnt/d/"),

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

