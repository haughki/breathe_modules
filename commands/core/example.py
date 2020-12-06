from commands.imports import *

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    None,
    # context = AppContext(executable="code"),
    mapping = {
        # "test <command> one" : Key("k"),
        "test <command> one" : Function(lambda command: Text("%s" % command).execute() if command else None),
        # "classy [<classtext>]"  : Text("class %(classtext)s:") + Key("left"),
    },
    extras = [
        Dictation("command", default=""),
        # Dictation("classtext", default="").title().replace(" ", ""),
    ]
)