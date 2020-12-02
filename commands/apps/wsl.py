from commands.imports import *
from supporting import utils

Breathe.add_commands(
    context = AppContext(executable='ubuntu') | AppContext(executable='WindowsTerminal'),
    mapping = {
        "project[s]": Text("proj") + Key("enter"),
        "Windows temp": Text("dtemp") + Key("enter"),
        "hawk user": Text("hawk") + Key("enter"),
        "mount delta": Text("/mnt/d/"),
        "mount Charlie": Text("/mnt/c/"),
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