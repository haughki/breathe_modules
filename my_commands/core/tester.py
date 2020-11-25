from dragonfly import *
from breathe import Breathe, CommandContext

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    context = AppContext(executable="code"),
    mapping = {
        "for each"              : Text("for  in :") + Key("left:5"),
        "for loop"              : Text("for i in range():") + Key("left:2"),
        # ------------------------------------------------
        "function [<snaketext>]": Text("def %(snaketext)s():") + Key("left:2"),
        "selfie [<snaketext>]"  : Text("self.%(snaketext)s"),
        "pointer [<snaketext>]" : Text(".%(snaketext)s"),
        "classy [<classtext>]"  : Text("class %(classtext)s:") + Key("left"),
    },
    extras = [
        Dictation("snaketext", default="").lower().replace(" ", "_"),
        Dictation("classtext", default="").title().replace(" ", ""),
    ]
)