from commands.imports import *
from . import specs
from supporting import utils


def defineGeneric(text, generic_type):
    formatted_text = ""
    if text:
        format_me = str(text)
        formatted_text = utils.text_to_case("pascal", format_me)
    Text(generic_type + formatted_text + "> ").execute()


def defineArrayList(text):
    defineGeneric(text, "ArrayList<")


def defineHashMap(text):
    defineGeneric(text, "HashMap<")


def getModifiers(words):
    modifiers_string = ""
    if len(words) > 0:
        modifiers = words
        for modifier in modifiers:
            modifiers_string = modifiers_string + modifier + " "
    return modifiers_string


def printModifiers(_node):
    Text(getModifiers(_node.words())).execute()


# def defineMethod(text, _node):
#     commands = _node.words()
#     method_index = commands.index("method")
#     modifiers_string = getModifiers(commands[:method_index])
#     formatted_class_name = ""
#     if text:
#         format_me = str(text)
#         if len(commands) > method_index + 1:
#             format_command = commands[method_index + 1]
#             if (format_command != "pascal") and (format_command !="snake"):
#                 format_command = "camel"  # default
#             formatted_class_name = utils.text_to_case(format_command, format_me)
#     (Text(modifiers_string + formatted_class_name + "() {") + Key("enter, up, end, left:3")).execute()

def define_method(access=None, static=None, final=None, void=None, casing=utils.camel, text=None):
    modifiers = ""
    if access: modifiers += access + " "
    if static: modifiers += static + " "
    if final: modifiers += final + " "
    if void: modifiers += void + " "

    end_text = Text("() {") + Key("enter, up, end, left:3")
    if text:
        assert callable(casing)
        (Text("%s%s" % (modifiers, casing(text))) + end_text).execute()

    else:
        (Text(modifiers) + end_text).execute()


def define_class(access=None, static=None, final=None, void=None, casing=utils.pascal, text=None):
    modifiers = ""
    if access: modifiers += access + " "
    if static: modifiers += static + " "
    if final: modifiers += final + " "
    if void: modifiers += void + " "

    end_text = Text(" {") + Key("enter")
    if text:
        assert callable(casing)
        (Text("%sclass %s" % (modifiers, casing(text))) + end_text).execute()

    else:
        (Text(modifiers) + end_text).execute()

def if_then(casing=utils.camel, text=None):
    if text:
        assert callable(casing)
        (Text("if (%s) {" % casing(text)) + Key("enter,up") + Key("c-right")).execute()
    else:
        (Text("if () {") + Key("enter,up")).execute()

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


INTELLIJ_POPUP_DELAY = "35"
Breathe.add_commands(
    context = AppContext(title=".java") | CommandContext("java"),
    mapping = {
        "define method [<access>] [<static>] [<final>] [<void>] [<casing>] [<text>]":
                                                              Function(define_method),
        "define class [<access>] [<static>] [<final>] [<casing>] [<text>]":
                                                              Function(define_class),
        "[(public | protected | private)] [static] [final]":  Function(printModifiers),
        "if then [<casing>] [<text>]":                        Function(if_then),
        "(shells | else) then":                               Text("else {") + Key("enter"),
        "(shells | else) if [<casing>] [<text>]":             Function(else_if),
        "(short | sue) if then [<casing>] [<text>]":          Function(short_if_then),
        "switch statement":                                   Key("dot, s, w, i, t, c, h/" + INTELLIJ_POPUP_DELAY + ", enter"),
        "case of":                                            Text("case :") + Key("left"),
        "breaker":                                            Text("break;"),
        "default":                                            Text("default: "),

        "print out":                                          Key("dot, s, o, u, t/" + INTELLIJ_POPUP_DELAY + ", enter"),
        "this":                                               Text("this"),
        # "for loop":                                          Text("for (int i=0; i< ; i++){") + Key("enter,up"),
        "for loop":                                           Key("dot, f, o, r, i/" + INTELLIJ_POPUP_DELAY + ", enter"),
        # "for each":                                          Text("for( : ){") + Key("enter,up"),
        "for each":                                           Key("dot, f, o, r/" + INTELLIJ_POPUP_DELAY + ", enter"),
        # "while loop":                                        Text("while ()")+Key("left"),
        "while loop":                                         Key("dot, w, h, i, l, e/" + INTELLIJ_POPUP_DELAY + ", enter"),
        "do loop":                                            Text("do {}") + Key("left, enter:2"),
        "try catch":                                          Key("dot, t, r, y/" + INTELLIJ_POPUP_DELAY + ", enter"),
        "try":                                                Text("try "),
        "catch":                                              Text("catch "),
        "finally":                                            Text("finally "),
        "throws":                                             Text("throws "),
        "throw":                                              Text("throw new "),

        "to integer":                     Text("Integer.parseInt()") + Key("left"),
        "to string":                      Text(".toString()"),
        "lodge and":                      Text(" && "),
        "lodge or":                       Text(" || "),
        "lodge not":                      Text("!"),
        "import":                         Text( "import " ),
        "here function":                  Text("() {")+Key("left"),
        "long comment":                   Text("/**/")+Key("left,left"),
        "nothing":                        Text("null"),
        "not nothing":                    Key("dot, n, u, l, l/" + INTELLIJ_POPUP_DELAY + ", enter"),
        "return":                         Key("dot, r, e, t, u, r, n/" + INTELLIJ_POPUP_DELAY + ", enter"),
        "true":                           Text("true"),
        "false":                          Text("false"),

        # "it are in": Text("Arrays.asList(TOKEN).contains(TOKEN)"),
        # "is not null": Key("dot, n, o, t, n, u, l, l/" + INTELLIJ_POPUP_DELAY + ", enter"),
        "create field": Key("dot, f, i, e, l, d/" + INTELLIJ_POPUP_DELAY + ", enter"),
        "try with resources": Key("dot, t, w, r/"  + INTELLIJ_POPUP_DELAY + ", enter"),
        "array to stream": Key("dot, s, t, r, e, a, m/" + INTELLIJ_POPUP_DELAY + ", enter"),
        "deco override": Text("@Override"),
        "generic list": Text("List<>") + Key("left"),
        "generic map": Text("Map<>") + Key("left"),
        "convert (array | hooray) to list": Text("Arrays.asList("),
        "new in line list": Text(" = new ArrayList<>(Arrays.asList());") + Key("left:3"),
        "(array | hooray) list [<text>]": Function(defineArrayList),
        "hash map [<text>]": Function(defineHashMap),

        # "substring": Text("substring"),
        # "cast to integer": Text("(int)()")+ Key("left"),
        # "(short | sue) shells": Text("else")+ Key("enter"),
        # "throw exception": Text("throw new Exception()")+ Key("left"),
        # "is instance of": Text(" instanceof "),
        "big integer": Text("Integer"),
        "big double": Text("Double"),
        "string": Text("String"),
        "becomes": Text(" -> "),
        "ternary": Text("()?:") + Key("left:3"),
        "is instance of": Key("dot, i, n, s, t/" + INTELLIJ_POPUP_DELAY + ", enter"),

        "new": Text("new "),
        "new me up": Key("space, equal, space, n, e, w, space/10, cs-space"),
        "continue": Text("continue"),
        "public": Text("public "),
        "private": Text("private "),
        "static": Text("static "),
        "final": Text("final "),
        "void": Text("void "),
        "abstract": Text("abstract "),
        "assert": Text("assert "),
        "go to": Text("goto "),
        "package": Text("package "),
        "synchronized": Text("synchronized "),
        "double": Text("double "),
        "implements": Text("implements "),
        "import": Text("import "),
        "enumeration": Text("enum "),
        "transient": Text("transient "),
        "extends": Text("extends "),
        "interface": Text("interface "),
        "volatile": Text("volatile "),
        "constant": Text("const "),
        "native": Text("native "),
        "super": Text("super "),

        "(bite | byte)": Text("byte "),
        "(integer | int)": Text("int "),
        "boolean": Text("boolean "),
        "(character | char)": Text("char "),
        "short": Text("short "),
        "long": Text("long "),
        "float": Text("float "),
        "char": Text("char "),
    },
    extras = [
        Dictation("modifiers"),
        Dictation("text"),
        Alternative((Literal("public"), Literal("private"), Literal("protected")), "access"),
        Literal("static", "static"),
        Literal("final", "final"),
        Literal("void", "void"),
        Choice("casing",
               {"snake": utils.snake, "snake up": utils.upper_snake, "camel": utils.camel, "Pascal": utils.pascal, "squash": utils.one_word, "squash up": utils.upper_one_word }),
    ],
    defaults = {
        "modifiers": None,
        "text": None,
    }
)

