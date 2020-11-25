from dragonfly import *
from supporting import utils

class Example(MappingRule):
    context = AppContext(executable="code")  # app-specific context
    #exported = False
    mapping = {
        "command one": Text("comm 1   "),
        "command two": Text("comm 2   "),
    }

class Example2(MappingRule):
    #exported = False
    mapping = {
        "command three": Text("comm 3   "),
        "command four": Text("comm 4   "),
    }


alternatives = [
    RuleRef(rule=Example()),
    RuleRef(rule=Example2()),
]
sequence = Repetition(Alternative(alternatives), min=1, max=16, name="sequence")
class ChainRule(CompoundRule):
    spec = "<sequence>"
    extras = [
        sequence,
    ]

    def _process_recognition(self, node, extras):
        for action in extras["sequence"]:
            action.execute()


example_grammar = Grammar("example grammar")
example_grammar.add_rule(ChainRule())
example_grammar.load()

def unload():
    global example_grammar
    example_grammar = utils.unloadHelper(example_grammar, __name__)