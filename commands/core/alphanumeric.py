from commands.imports import *

nato_alphabet = {
    "Alpha": "a",
    "Bravo": "b",
    "Charlie": "c",
    "Delta": "d",
    "Echo": "e",
    "Foxtrot": "f",
    "Gumbo": "g",
    "Honda": "h",
    "Igloo": "i",
    "Juneau": "j",
    "Kilo": "k",
    "Lima": "l",
    "Monty": "m",
    "Ninja": "n",
    "Oscar": "o",
    "Papa": "p",
    "Quinn": "q",
    "Robin": "r",
    "Soda": "s",
    "Tango": "t",
    "Urdu": "u",
    "Victor": "v",
    "Whiskey": "w",
    "X-ray": "x",
    "Yankee": "y",
    "Zulu": "z",
}

Breathe.add_commands(
    None,
    {
        "[<big>] <letter>": Function(
            lambda big, letter: Text(letter.upper() if big else letter).execute()
        ),
        "numb <num_seq>": Function(lambda num_seq: Text("".join(map(str, num_seq)))),
    },
    [
        Choice("big", {"big": True}, default=False),
        Choice("letter", nato_alphabet),
        Repetition(IntegerRef("", 0, 10), min=1, max=6, name="num_seq"),
    ]
)
