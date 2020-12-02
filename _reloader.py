import os

from dragonfly import *
from reimport import reimport

from supporting import utils, character

# putstringcommands is not included in the pushed source, because it contains personal data.
try:
    from ccr import putstringcommands
except ImportError:
    pass



MACROSYSTEM_DIRECTORY = "C:\\breathe_modules"

def characterReloader():
    print "Reloading character..."
    reimport(character)
    utils.toggleMicrophone()

def utilsReloader():
    print "Reloading utils..."
    reimport(utils)
    utils.toggleMicrophone()

class ReloadRule(MappingRule):
    mapping = {
        "reload character": Function(characterReloader),
        "reload utilities": Function(utilsReloader),
    }

reload_grammar = Grammar("reloading grammar")
reload_grammar.add_rule(ReloadRule())
reload_grammar.load()

def unload():
    global reload_grammar
    reload_grammar = utils.unloadHelper(reload_grammar, __name__)