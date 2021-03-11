from commands.imports import *

Breathe.add_commands(
    None,
    mapping = {
        "one close": Key("c-c, del, {, {, c, 1, colon, colon, c-v, backspace, }, }, space"),
        "two close": Key("c-c, del, {, {, c, 2, colon, colon, c-v, backspace, }, }, space"),

        "Jean pass": Key("ca-j"),
        # "clean close [<n>]": Key("c-a, del, c-w/20:%(n)d"),stop
    }
)
