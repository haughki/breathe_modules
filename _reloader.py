from dragonfly import *
from breathe import *
from reimport import reimport

from supporting import utils, character
from commands.languages import specs, python_bindings


rebuild_these = (
    utils,
    character,
    specs,
    python_bindings
)

def rebuild_all():
    extras_rebuilder()
    Breathe.reload_modules()
    Key("npadd/10,npadd").execute() # toggle microphone to rebuild non-breathe modules.

def extras_rebuilder():
    print "Rebuilding extras..."
    for rebuild_me in rebuild_these:
        print(rebuild_me)
        reimport(rebuild_me)
    utils.toggleMicrophone()

# def specsRebuilder():
#     print "Rebuilding specs..."
#     reimport(specs)
#     utils.toggleMicrophone()
#
# def characterRebuilder():
#     print "Rebuilding character..."
#     reimport(character)
#     utils.toggleMicrophone()
#
# def utilsRebuilder():
#     print "Rebuilding utils..."
#     reimport(utils)
#     utils.toggleMicrophone()

class RebuildRule(MappingRule):
    mapping = {
        "rebuild extras": Function(extras_rebuilder),
        "rebuild all": Function(rebuild_all),
        # "rebuild specs": Function(specsRebuilder),
        # "rebuild character": Function(characterRebuilder),
        # "rebuild utilities": Function(utilsRebuilder),
    }

rebuild_grammar = Grammar("rebuilding grammar")
rebuild_grammar.add_rule(RebuildRule())
rebuild_grammar.load()

def unload():
    global rebuild_grammar
    rebuild_grammar = utils.unloadHelper(rebuild_grammar, __name__)