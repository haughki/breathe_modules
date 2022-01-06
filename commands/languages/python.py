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
        (Text("def (self):") + Key("left:7")).execute()

def define_private_method(text=None):
    define_method("_" + text)

def define_class(text=None):
    if text:
        text = utils.pascal(text)
        (Text("class " + text + ":") + Key("left")).execute()
    else:
        (Text("class :") + Key("left")).execute()

def make_private(text):
    text = "_" + utils.snake(text)
    (Text(text)).execute()

def if_then(casing=utils.snake, text=None):
    if text:
        assert callable(casing)
        (Text("if %s:" % casing(text)) + Key("enter")).execute()
    else:
        (Text("if :") + Key("left")).execute()

Breathe.add_commands(
    context = AppContext(title=".py") | CommandContext("python"),
    mapping = {
        "define class [camel | snake] [<text>]":              Function(define_class),
        "define method [<text>]":                             Function(define_method),
        "define private method [<text>]":                     Function(define_private_method),
        "define function [<text>]":                           Function(define_function),
        "define initializer":                                 Text("def __init__(self):") + Key("left:2"),
        "private <text>":                                     Function(make_private),
        "if then [<casing>] [s<text>]":                        Function(if_then),
        "else then":                               Text("else:") + Key("enter"),
        "if else":                                 Key("i,f,space,colon,enter,s-tab,e,l,s,e,colon,up,left"),
        "else if":                                 Key("e,l,i,f,space,colon,left"),
        "inline if":                                          Text(" if  else ") + Key("left:6"),
        "list comprehension":                                 Text("[x for x in if ]"),

        "print out":                      Text("print()") + Key("left"),
        "self":                           Text("self"),
        "for loop":                       Text("for i in range(0, ):") + Key("left:2"),
        "for each":                       Text("for in :") + Key("left:4"),
        "breaker":                        Text("break"),
        "while loop":                     Text("while :") + Key("left"),
        "with":                           Text("with "),
        "with open":                      Text("with open()") + Text(" as f") + Key("colon/3, left:7"),
        # "read lines":                   Text("content = f.readlines()"),
        "try catch":                      Text("try:") + Key("enter:2, backspace") + Text("except Exception:") + Key("enter, up, up"),
        "except":                         Text("except :") + Key("left"),
        "finally":                        Text("finally:") + Key("enter"),
        "raise":                          Text("raise "),

        "to string":                      Text("str()") + Key("left"),
        "to integer":                     Text("int()") + Key("left"),
        "to float":                       Text("float()") + Key("left"),
        "to (character | char)":          Text("chr()") + Key("left"),
        "to dictionary":                  Text("dict()") + Key("left"),
        "to list":                        Text("list()") + Key("left"),
        "to (topple | tuple)":            Text("tuple()") + Key("left"),
        "length":                         Text("len()") + Key("left"),

        "lodge and":                    Text(" and "),
        "lodge as":                     Text(" as "),
        "lodge (shells | else)":        Text(" else "),
        "lodge if":                     Text(" if "),
        # "lodge in":                     Text(" in "),
        "is in":                        Text(" in "),
        "lodge is":                     Text(" is "),
        "is not":                 Text(" is not "),
        "lodge not":                    Text(" not "),
        "not in":                 Text(" not in "),
        "lodge or":                     Text(" or "),
        "lodge for":                      Text(" for "),
        "not nothing":                    Text(" not None"),
        "is not nothing":                 Text(" is not None"),
        "true":                           Text("True"),
        "false":                          Text("False"),
        "nothing":                        Text("None"),

        # "and":                            Text(" and "),
        # "as":                             Text(" as "),
        # "(shells | else)":                Text(" else "),
        # "if":                             Text(" if "),
        # "in":                             Text(" in "),
        # "is":                             Text(" is "),
        # "is not":                         Text(" is not "),
        # "not":                            Text(" not "),
        # "not in":                         Text(" not in "),
        # "or":                             Text(" or "),
        # "for":                          Text(" for "),

        "import":                         Text("import "),
        "return":                         Text("return "),
        "from":                           Text("from "),
        "global":                         Text("global "),
        "assert":                         Text("assert "),
        "async":                          Text("async"),
        "await":                          Text("await"),
        "continue":                       Text("continue"),
        "delete":                         Text("del "),
        "lambda":                         Text("lambda :") + Key("left"),
        "non-local":                      Text("nonlocal"),
        "pass":                           Text("pass"),
        "yield":                          Text("yield"),

        "add comment":                    Text( "#" ),
        "long comment":                   Text("\"\"\""),
        "[dot] (pie | pi)":               Text(".py"),

        "dot method <method>":            Text(".%(method)s()") + Key("left"),
        "built-in <builtin>":             Text("%(builtin)s()") + Key("left"),
        "type <type>":                    Text("%(type)s"),
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
