from dragonfly import *
from supporting import utils

class Example(MappingRule):
    context = AppContext(executable="code")  # app-specific context
    #exported = False
    mapping = {
        "command one": Text("comm 1   "),
        "command two": Text("comm 2   "),
    }

example_grammar = Grammar("example grammar")
example_grammar.add_rule(Example())
example_grammar.load()

def unload():
    global example_grammar
    example_grammar = utils.unloadHelper(example_grammar, __name__)