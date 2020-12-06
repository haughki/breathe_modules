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


Breathe.add_commands(
        context = AppContext(title=".py") | CommandContext("python"),
        mapping = {
            "(shells | else) if":                   Key("e,l,i,f,space,colon,left"),
            # specs.SymbolSpecs.IF:                   Key("i,f,space,colon,left"),
           "if [<text>] then":                      Function(lambda text: (
                                                        (Text("if %s:" % text) + Key("enter")).execute() if text else (Text("if :") + Key("left")).execute()
                                                    )),
            specs.SymbolSpecs.ELSE:                 Text("else:") + Key("enter"),
            "if (shells | else)":              Key("i,f,space,colon,enter,s-tab,e,l,s,e,colon,up,left"),
            "define method [<text>]":        Text("def ():") + Key("left:3"),
            "define function [<text>]":             Function(define_function),
            "define self":                          Text("def (self):") + Key("left:7"),
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
            "self":                         Text("self"),
            # "long not":                     Text(" not "),
            "it are in":                    Text(" in "),          #supposed to sound like "iter in"
            # "shell iffae | LFA":            Key("e,l,i,f,space,colon,left"),

            "global":                       Text("global "),
            "list comprehension":           Text("[x for x in if ]"),
            "[dot] (pie | pi)":             Text(".py"),
            "identity is":                  Text(" is "),
            "is instance":                  Text(" isinstance()") + Key("left"),
            "length ":                      Text("len()") + Key("left"),

            "dot meth <method>":              Text(".%(method)s()") + Key("left"),
            # "built-in <builtin>":              Text(".%(method)s()") + Key("left"),
        },
    extras = [
        Dictation("modifiers"),
        Dictation("text", default=""),
        Choice("method", python_bindings.methods),
    ],
    defaults = {
        "modifiers": None,
    }
)
