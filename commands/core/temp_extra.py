from commands.imports import *
from dragonfly.windows.clipboard import Clipboard


def add_close(_node):
    number = _node.words()[0]
    if number == "one":
        number = "1"
    else:
        number = "2"
    close_start = "{{c" + number + "::"

    Key("c-c, del").execute()
    # Key("c-c").execute()
    clipboard = Clipboard()
    clipboard.copy_from_system()
    print(clipboard)
    close_word = clipboard.get_text()

    last = close_word[-1]
    second_to_last = close_word[-2]

    s = ""
    if last == " ":
        if second_to_last == "," or second_to_last == ".":
            s = close_start + close_word[:-2] + "}}" + second_to_last + " "
        else:
            s = close_start + close_word[:-1] + "}}" + " "
    elif last == "," or last == ".":
        s = close_start + close_word[:-1] + "}}" + last
    else:
        s = close_start + close_word + "}}"

    # Text("{{c" + number + "::" + close_word[:-2] + "}}" + second_to_last + " ").execute()
    # Text("{{c" + number + "::" + close_word[:-1] + "}} ").execute()

    if s != "":
        Paste(s).execute()

Breathe.add_commands(
    None,
    mapping = {
        # "one close": Key("c-c, del, {, {, c, 1, colon, colon, c-v, backspace, }, }, space"),
        "(one | two) close": Function(add_close),
        # "two close": Key("c-c, del, {, {, c, 2, colon, colon, c-v, backspace, }, }, space"),

        "Jean pass": Key("ca-j"),
        # "clean close [<n>]": Key("c-a, del, c-w/20:%(n)d"),stop
    }
)
