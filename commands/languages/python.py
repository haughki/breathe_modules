from commands.imports import *
import specs, python_bindings
from supporting import utils

def define_function(text=None):
    if text:
        text = utils.snake(text)
        (Text("def " + text + "():") + Key("left:2")).execute()
    else:
        (Text("def ():") + Key("left:3")).execute()

def define_method(text=None):
    if text:
        text = utils.snake(text)
        (Text("def " + text + "(self):") + Key("left:2")).execute()
    else:
        (Text("def (self):") + Key("left:3")).execute()


def define_class(text=None):
    if text:
        text = utils.pascal(text)
        (Text("class " + text + "():") + Key("left:2")).execute()
    else:
        (Text("class ():") + Key("left:3")).execute()

def if_then(casing=utils.snake, text=None):
    if text:
        assert callable(casing)
        (Text("if %s:" % casing(text)) + Key("enter")).execute()
    else:
        (Text("if :") + Key("left")).execute()

Breathe.add_commands(
        context = AppContext(title=".py") | CommandContext("python"),
        mapping = {
            "(shells | else) if":                   Key("e,l,i,f,space,colon,left"),
            # specs.SymbolSpecs.IF:                   Key("i,f,space,colon,left"),
           "if [<casing>] [<text>] then":                      Function(if_then),
            specs.SymbolSpecs.ELSE:                 Text("else:") + Key("enter"),
            "if (shells | else)":              Key("i,f,space,colon,enter,s-tab,e,l,s,e,colon,up,left"),
            "define method [<text>]":               Function(define_method),
            "define function [<text>]":             Function(define_function),
            specs.SymbolSpecs.FOR_LOOP:             Text("for i in range(0, ):") + Key("left:2"),
            specs.SymbolSpecs.FOR_EACH_LOOP:        Text("for in :") + Key("left:4"),
            specs.SymbolSpecs.SYSOUT:               Text("print()") + Key("left"),


            "with":                         Text("with "),
            # "open file":                    Text("open('filename','r') as f:"),
            # "read lines":                   Text("content = f.readlines()"),
            # "try catch":                    Text("try:")+Key("enter:2/10, backspace")+Text("except Exception:")+Key("enter"),

            specs.SymbolSpecs.BREAK:              Text("break"),
            specs.SymbolSpecs.WHILE_LOOP:         Text("while :")+ Key("left"),

            specs.SymbolSpecs.TO_STRING:          Text("str()") + Key("left"),
            specs.SymbolSpecs.TO_INTEGER:         Text("int()")+ Key("left"),
            specs.SymbolSpecs.TO_FLOAT:           Text("float()")+ Key("left"),
            "to (character | char)":              Text("chr()")+ Key("left"),
            "to dictionary":              Text("dict()")+ Key("left"),
            "to list":              Text("list()")+ Key("left"),
            "to (topple | tuple)":              Text("tuple()")+ Key("left"),
            "length ":                      Text("len()") + Key("left"),

            specs.SymbolSpecs.AND:                Text(" and "),
            specs.SymbolSpecs.OR:                 Text(" or "),
            specs.SymbolSpecs.NOT:                Text(" not "),

            specs.SymbolSpecs.IMPORT:             Text( "import " ),
            specs.SymbolSpecs.CLASS:              Function(define_class),
            specs.SymbolSpecs.COMMENT:            Text( "#" ),
            specs.SymbolSpecs.LONG_COMMENT:       Text("\"\"\""),
            specs.SymbolSpecs.NOT_EQUAL_NULL:     Text(" not None"),
            specs.SymbolSpecs.NULL:               Text("None"),
            specs.SymbolSpecs.RETURN:             Text("return "),
            specs.SymbolSpecs.TRUE:               Text("True"),
            specs.SymbolSpecs.FALSE:              Text("False"),

            # "sue iffae":                    Text("if "),
            # "sue shells":                   Text("else "),

            "from":                         Text( "from " ),
            "global":                       Text("global "),
            "it are in":                    Text(" in "),          #supposed to sound like "iter in"
            "identity is":                  Text(" is "),
            "self":                         Text("self"),

            "list comprehension":           Text("[x for x in if ]"),
            "[dot] (pie | pi)":             Text(".py"),
            # "is instance":                  Text(" isinstance()") + Key("left"),

            "dot meth <method>":              Text(".%(method)s()") + Key("left"),
            "built-in <builtin>":              Text("%(builtin)s()") + Key("left"),
            "type <type>":              Text("%(type)s"),
        },
    extras = [
        Dictation("modifiers", default=None),
        Dictation("text", default=""),
        Choice("casing",
               {"snake": utils.snake, "snake up": utils.upper_snake, "camel": utils.camel, "Pascal": utils.pascal, "squash": utils.one_word, "squash up": utils.upper_one_word }),
        Choice("method", python_bindings.methods),
        Choice("builtin", python_bindings.builtins),
        Choice("type", python_bindings.types),
    ]
)
