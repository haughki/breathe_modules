from dragonfly import *
from reimport import reimport

from supporting import utils, character
from commands.languages import specs, python_bindings

MACROSYSTEM_DIRECTORY = "C:\\breathe_modules"

reload_these = (
    utils,
    character,
    specs,
    python_bindings
)

def extrasReloader():
    print "Reloading extras..."
    for reload_me in reload_these:
        print(reload_me)
        reimport(reload_me)
    utils.toggleMicrophone()

# def specsReloader():
#     print "Reloading specs..."
#     reimport(specs)
#     utils.toggleMicrophone()
#
# def characterReloader():
#     print "Reloading character..."
#     reimport(character)
#     utils.toggleMicrophone()
#
# def utilsReloader():
#     print "Reloading utils..."
#     reimport(utils)
#     utils.toggleMicrophone()

class ReloadRule(MappingRule):
    mapping = {
        "reload extras": Function(extrasReloader),
        # "reload specs": Function(specsReloader),
        # "reload character": Function(characterReloader),
        # "reload utilities": Function(utilsReloader),
    }

reload_grammar = Grammar("reloading grammar")
reload_grammar.add_rule(ReloadRule())
reload_grammar.load()

def unload():
    global reload_grammar
    reload_grammar = utils.unloadHelper(reload_grammar, __name__)