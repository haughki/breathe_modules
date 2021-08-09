from commands.imports import *
#import specs, python_bindings
from supporting import utils

def define_function(text=None):
    if text:
        text = utils.camel(text)
        (Text("function " + text + "() {") + Key("left:3")).execute()
    else:
        (Text("function () {") + Key("left:4")).execute()

def define_method(text=None):
    if text:
        text = utils.camel(text)
        (Text("def " + text + "(self):") + Key("left:2")).execute()
    else:
        (Text("def (self):") + Key("left:7")).execute()

# def define_private_method(text=None):
#     define_method("_" + text)

def define_class(text=None):
    if text:
        text = utils.pascal(text)
        (Text("class " + text + " {") + Key("left:2")).execute()
    else:
        (Text("class  {") + Key("left:2")).execute()

def if_then(casing=utils.camel, text=None):
    if text:
        assert callable(casing)
        (Text("if (%s) {" % casing(text)) + Key("enter,up") + Key("c-right")).execute()
    else:
        (Text("if () {") + Key("enter,up,right:2")).execute()

def short_if_then(casing=utils.camel, text=None):
    if text:
        assert callable(casing)
        (Text("if (%s)" % casing(text)) + Key("left")).execute()
    else:
        (Text("if ()") + Key("left")).execute()

def else_if(casing=utils.camel, text=None):
    if text:
        assert callable(casing)
        (Text(" else if (%s) {" % casing(text)) + Key("enter,up") + Key("c-right:4")).execute()
    else:
        (Text(" else if () {") + Key("enter,up,c-right:3")).execute()


Breathe.add_commands(
    context = AppContext(title=".js") | CommandContext("javascript"),
    mapping = {
        "define class [camel | snake] [<text>]":              Function(define_class),
        "define method [<text>]":                             Function(define_method),
        "define function [<text>]":                           Function(define_function),
        "if then [<casing>] [<text>]":                        Function(if_then),
        "(shells | else) then":                               Text("else {") + Key("enter"),
        "(shells | else) if [<casing>] [<text>]":             Function(else_if),
        "(short | sue) if then [<casing>] [<text>]":          Function(short_if_then),
        # "switch statement":                                   Key("dot, s, w, i, t, c, h/" + INTELLIJ_POPUP_DELAY + ", enter"),
        "case of":                                            Text("case :") + Key("left"),
        "breaker":                                            Text("break;"),
        "default":                                            Text("default: "),


        "print out":                      Text("console.log()") + Key("left"),
        "this":                           Text("this"),
        "for loop":                                          Text("for (let i = 0; i < ; i++){") + Key("enter,up,end,left:7"),
        "for each":                                          Text(".forEach( =>)") + Key("left,enter,up,end,left:3"),
        "while loop":                                        Text("while ()")+Key("left"),
        "do loop":                                            Text("do {}") + Key("left, enter:2"),
        "try":                                                Text("try "),
        "catch":                                              Text("catch "),
        "finally":                                            Text("finally "),
        "throw":                                              Text("throw new "),
        "let":                                              Text("let "),
        "constant":                                              Text("const "),

        # "to string":                      Text("str()") + Key("left"),
        # "to integer":                     Text("int()") + Key("left"),
        # "to float":                       Text("float()") + Key("left"),
        # "to (character | char)":          Text("chr()") + Key("left"),
        # "to dictionary":                  Text("dict()") + Key("left"),
        # "to list":                        Text("list()") + Key("left"),
        # "to (topple | tuple)":            Text("tuple()") + Key("left"),
        # "length":                         Text("len()") + Key("left"),

        "lodge and":                    Text(" and "),
        "lodge as":                     Text(" as "),
        "lodge (shells | else)":        Text(" else "),
        "lodge and":                      Text(" && "),
        "lodge or":                       Text(" || "),
        "lodge not":                      Text("!"),
        "lodge if":                     Text(" if "),
        # "lodge in":                     Text(" in "),
        # "is in":                        Text(" in "),
        "lodge for":                      Text(" for "),
        "is not nothing":             Text(" !== null"),
        "true":                           Text("true"),
        "false":                          Text("false"),
        "nothing":                        Text("null"),

        "ternary":                        Text("()?:") + Key("left:3"),
        "import":                         Text("import "),
        "export":                         Text("export "),
        "return":                         Text("return "),
        "from":                           Text("from "),
        # "global":                         Text("global "),
        "assert":                         Text("assert "),
        "async":                          Text("async"),
        "await":                          Text("await"),
        "continue":                       Text("continue"),
        # "delete":                         Text("del "),
        "lambda":                         Text(" => ") + Key("left"),
        "lambda funk":                    Text("() => {") + Key("left:6"),

        "add comment":                    Text("//"),
        "long comment":                   Text("/* */"),

        # "dot method <method>":            Text(".%(method)s()") + Key("left"),
        # "built-in <builtin>":             Text("%(builtin)s()") + Key("left"),
        # "type <type>":                    Text("%(type)s"),
    },
    extras = [
        Dictation("modifiers", default=None),
        Dictation("text", default=""),
        Choice("casing",
               {"snake": utils.snake, "snake up": utils.upper_snake, "camel": utils.camel, "Pascal": utils.pascal, "squash": utils.one_word, "squash up": utils.upper_one_word }),
        # Choice("method", python_bindings.methods),
        # Choice("builtin", python_bindings.builtins),
        # Choice("type", python_bindings.types),
    ]
)
