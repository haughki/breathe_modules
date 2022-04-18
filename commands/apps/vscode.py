# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=8282, stdoutToServer=True, stderrToServer=True)


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

        # Code execution.
        # "run app": Key("s-f10"),
        # "stop app": Key("c-f2"),
        "disconnect debugging": Key("s-f9"),
        "stop debugging": Key("s-f5"),
        "debug app": Key("f9"),
        "debug restart": Key("cs-f9"),
        # "re-run app": Key("c-f5"),
        # "run this [app]": Key("cs-f10"),
        # "run test": Key("cs-f10"),
        "[toggle] (breakpoint | break)": Key("f5"),
        "stop running": Key("s-f5"),
        "step [over]": Key("f10"),
        "step into": Key("f11"),
        "step out": Key("s-f11"),
        "(keep running | resume)": Key("f9"),

        # Search.
        "replace": Key("c-r"),
        "replace (enter | all)": Key("ca-enter"),
        "show find": Key("c-f"),
        # "find <text>": Key("c-f/25") + Text("%(text)s"),
        "find next": Key("f3"),
        "find (prev | previous)": Key("s-f3"),
        "find in files": Key("cs-f"),

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
        "next (book | bookmark)": Key("ca-0"),
        "(prev | previous) book": Key("ca-8"),

        # Window handling.
        "new tab": Key("c-n"),
        "next tab [<t>]": Key("c-pagedown:%(t)d"),
        "preev tab [<t>]": Key("c-pageup:%(t)d"),
        "close tab [<t>]": Key("c-w:%(t)d"),

        "(full-screen | full screen)": Key("cs-x"),
        "(hide | hi | show) sidebar": Key("c-b"),
        "(hide | hi | show) bottom": Key("cs-j"),
        "go to editor": Key("csa-`"),
        "go to sidebar": Key("c-0"),
        "go to bottom": Key("c-`"),
        "sidebar file": Key("cs-\\"),

        # Code
        "format file": Key("as-f"),

        # Refactoring
        # "(refactor|re-factor) (this|choose)": Key("cas-t"),
        "[(refactor|re-factor)] rename": Key("f2"),
        "rename [current] file": Key("c-0") + Key("f2"),
        # "[(refactor|re-factor)] change signature": Key("c-f6"),
        # "(refactor|re-factor) move": Key("f6"),
        # "(refactor|re-factor) copy": Key("f5"),
        # "[(refactor|re-factor)] safe delete": Key("a-del"),
        # "[(refactor|re-factor)] extract constant": Key("ca-c"),
        # "[(refactor|re-factor)] extract field": Key("ca-f"),
        # "[(refactor|re-factor)] extract parameter": Key("ca-p"),
        # "[(refactor|re-factor)] extract variable": Key("ca-v"),
        # "[(refactor|re-factor)] extract method": Key("ca-w"),
        # "[(refactor|re-factor)] (in line|inline)": Key("ca-n"),


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
