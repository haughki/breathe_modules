from my_commands.imports import *

Breathe.add_commands(
    context=None,
    mapping={
        "hello world [<n>]": Text("Hello world!") * Repeat("n")
    },
    extras=[
        IntegerRef("n", 1, 10, default=1),
    ]
)