"""A command module for Dragonfly, for controlling VSCode.
-----------------------------------------------------------------------------
Licensed under the LGPL3.

"""

from commands.imports import *
from supporting import utils

def getFile(text=None):
    open_get_file_dialog = Key("c-p")
    if text:
        open_get_file_dialog.execute()
        file_name = str(text).lower()
        Text(file_name).execute()
    else:
        open_get_file_dialog.execute()

Breathe.add_commands(
    context = AppContext(executable='code'),
    mapping = {
        # misc
        "do command": Key("cs-p"),
        "run app": Key("ca-n"),
        "jump": Key("c-semicolon"),
        "select jump": Key("ca-comma"),

       #"[go to | show] project window": Key("a-1"),

        # Search.
        "replace": Key("c-r"),
        "replace (enter | all)": Key("ca-enter"),
        "show find": Key("c-f"),
        "find <text>": Key("c-f/25") + Text("%(text)s"),
        # "find next": Key("f3"),
        # "find (prev | previous)": Key("s-f3"),
        # "find in files": Key("cs-f"),

        # Edit.
        "[shoreline | show] line <w> [<x>] [<y>] [<z>]": Key("c-g/25") + Function(utils.printNumber) + Key("enter"),
        "[show] white space": Key("cs-w"),
        "word wrap": Key("cs-d"),
        "comment [line | that | it]": Key("c-slash"),
        # "scroll up [<n>]": Key("a-up:%(n)d"),      # Something about these two scroll commands causes NatLink to hang when I switch to VS code
        # "scroll down [<n>]": Key("a-down:%(n)d"),  # Something about these two scroll commands causes NatLink to hang when I switch to VS code
        "move line up [<n>]": Key("c-up:%(n)d"),
        "move line down [<n>]": Key("c-down:%(n)d"),

        # Code navigation.
        "get file [<text>]": Function(getFile),  # "Navigate > File..."
        "toggle (book | bookmark)": Key("f7"),
        "next (book | bookmark)": Key("cs-n"),
        "(prev | previous) book": Key("cs-p"),

        # Window handling.
        "new tab": Key("c-n"),
        "next tab [<t>]": Key("c-pagedown:%(t)d"),
        "preev tab [<t>]": Key("c-pageup:%(t)d"),
        "close tab": Key("c-w"),
        "(full-screen | full screen)": Key("cs-x"),
        "(toggle | show) sidebar": Key("c-b"),
        "go to sidebar": Key("c-0"),
        "go to editor": Key("csa-`"),
        "rename [current] file": Key("c-0") + Key("f2"),
        "sidebar rename": Key("f2"),

        # git
        "pull this": Key("c-t"),
        "push this": Key("c-k"),

        # Ansible
        # "define variable": Text("- set_fact:\n\t\t"),
        # "debug variable": Text("- debug: var="),
        # "debug message": Text("- debug: \n\t\tmsg: "),
        # "extract variable": Text("\"{{}}\"") + Key("left:3")
    },

    extras = [
        Integer("t", 1, 50),
        Dictation("text"),
        IntegerRef("n", 1, 50000),
        Integer("w", 0, 10),
        Integer("x", 0, 10),
        Integer("y", 0, 10),
        Integer("z", 0, 10)
    ],
    defaults = {
        "t": 1,
        "n": 1,
    }
)
