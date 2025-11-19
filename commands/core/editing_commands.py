# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=8282, stdoutToServer=True, stderrToServer=True)


from commands.imports import *
from supporting import character, utils



""" Converts a lowercase char to uppercase. The 'letters_ref' is defined in the 'extras' of the mapping rule.
    The 'ref' makes it possible to pass the dictated value (e.g., "Alpha") to this Function action."""
def convert_to_upper(letters_ref):  # Note, the parameter name here has to match the value of the 'name' member of the ListRef.
    Key(character.CHARACTER_MAP[letters_ref].upper()).execute()

letters = List("letters_list", [
    character.A, character.B, character.C, character.D, character.E, character.F, character.G, character.H, character.I, character.J, character.K, character.L, character.M, character.N, character.O, character.P, character.Q, character.R, character.S, character.T, character.U, character.V, character.W, character.X, character.Y, character.Z
])
letters_reference = ListRef("letters_ref", letters)


def mark_block(a, w, b=None, c=None, d=None, x=None, y=None, z=None):
    num1 = int(utils.buildNumber(a, b, c, d))
    num2 = int(utils.buildNumber(w, x, y, z))
    Key("shift:down").execute()
    Key("down:" + str(num2 - num1 + 1)).execute()

# def mark_block(m, n):
#     Key("shift:down").execute()
#     Key("down:" + str(m - n + 1)).execute()

def acronym(c1, c2, c3=None, c4=None, c5=None, c6=None):
    acro = ""
    acro += character.NAMED_CHARACTER_MAP[c1].upper()
    acro += character.NAMED_CHARACTER_MAP[c2].upper()
    acro += character.NAMED_CHARACTER_MAP[c3].upper() if c3 else ""
    acro += character.NAMED_CHARACTER_MAP[c4].upper() if c4 else ""
    acro += character.NAMED_CHARACTER_MAP[c5].upper() if c5 else ""
    acro += character.NAMED_CHARACTER_MAP[c6].upper() if c6 else ""
    Text(acro).execute()

#---------------------------------------------------------------------------
# Here we globally defined the release action which releases all modifier-keys used within this grammar.  It is defined here
#  because this functionality is used in many different places. Note that it is harmless to release ("...:up") a key multiple
#  times or when that key is not held down at all.
release = Key("shift:up, ctrl:up, alt:up")

Breathe.add_commands(
    None,
    mapping={
        # Spoken-form    ->    ->    ->     Action object

        #### Dragon
        "Snork": Key("npadd/10,npadd"),  # turn mic on and off
        "(Mike | mic) off": Key("npadd"),  # turn mic off
        "(Mike | mic) sleep": Key("npdiv"),

        #### Cursor manipulation
        "cup [<n>]": Key("up:%(n)d"),
        "down [<n>]": Key("down:%(n)d"),
        "left [<n>]": Key("left:%(n)d"),
        "right [<n>]": Key("right:%(n)d"),
        "tope [<n>]": Key("pgup:%(n)d"),
        "drop [<n>]": Key("pgdown:%(n)d"),
        "(port | Lefty | word left) [<n>]": Key("c-left:%(n)d"),
        "(yope | word right | righty) [<n>]": Key("c-right:%(n)d"),
        "home [<n>]": Key("home:%(n)d"),
        "kick [<n>]": Key("end:%(n)d"),
        "top": Key("c-home"),
        "toe": Key("c-end"),
        "make line": Key("up, end, enter"),
        "(scroll | page) up [<n>]": Key("c-up:%(n)d"),
        "(scroll | page) down [<n>]": Key("c-down:%(n)d"),

        #### Various keys
        character.SPACE       + " [<n>]": Key("space:%(n)d"),
        character.TAB         + " [<n>]": Key("tab:%(n)d"),
        character.S_TAB       + " [<n>]": Key("s-tab:%(n)d"),
        character.ENTER       + " [<n>]": Key("enter:%(n)d"),
        character.DEL         + " [<n>]": Key("del:%(n)d"),
        character.BACKSPACE   + " [<n>]": Key("backspace:%(n)d"),
        character.ESCAPE      + " [<n>]": Key("escape:%(n)d"),

        character.AMPERSAND   + " [<n>]": Key("ampersand:%(n)d"),
        character.APOSTROPHE  + " [<n>]": Key("apostrophe:%(n)d"),
        character.ASTERISK    + " [<n>]": Key("asterisk:%(n)d"),
        character.AT          + " [<n>]": Key("at:%(n)d"),
        character.BACKSLASH   + " [<n>]": Key("backslash:%(n)d"),
        character.BACKTICK    + " [<n>]": Key("backtick:%(n)d"),
        character.BAR         + " [<n>]": Key("bar:%(n)d"),
        character.CARET       + " [<n>]": Key("caret:%(n)d"),
        character.COLON       + " [<n>]": Key("colon:%(n)d"),
        character.HYPHEN      + " [<n>]": Key("hyphen:%(n)d"),
        character.COMMA       + " [<n>]": Key("comma:%(n)d"),
        character.DOLLAR      + " [<n>]": Key("dollar:%(n)d"),
        character.DOT         + " [<n>]": Key("dot:%(n)d"),
        character.DQUOTE      + " [<n>]": Key("dquote:%(n)d"),
        character.EQUAL       + " [<n>]": Key("equal:%(n)d"),
        character.EXCLAMATION + " [<n>]": Key("exclamation:%(n)d"),
        character.HASH        + " [<n>]": Key("hash:%(n)d"),
        character.POUND       + " [<n>]": Key("hash:%(n)d"),
        character.PERCENT     + " [<n>]": Key("percent:%(n)d"),
        character.PLUS        + " [<n>]": Key("plus:%(n)d"),
        character.PRINTSCREEN + " [<n>]": Key("printscreen:%(n)d"),
        character.QUESTION    + " [<n>]": Key("question:%(n)d"),
        character.SLASH       + " [<n>]": Key("slash:%(n)d"),
        character.SQUOTE      + " [<n>]": Key("squote:%(n)d"),
        character.TILDE       + " [<n>]": Key("tilde:%(n)d"),
        character.UNDERSCORE  + " [<n>]": Key("underscore:%(n)d"),
        character.SEMICOLON   + " [<n>]": Key("semicolon:%(n)d"),
        character.LANGLE      + " [<n>]": Key("langle:%(n)d"),
        character.RANGLE      + " [<n>]": Key("rangle:%(n)d"),
        character.LBRACE      + " [<n>]": Key("lbrace:%(n)d"),
        character.RBRACE      + " [<n>]": Key("rbrace:%(n)d"),
        character.LBRACKET    + " [<n>]": Key("lbracket:%(n)d"),
        character.RBRACKET    + " [<n>]": Key("rbracket:%(n)d"),
        character.LPAREN      + " [<n>]": Key("lparen:%(n)d"),
        character.LPAREN2     + " [<n>]": Key("lparen:%(n)d"),
        character.LPAREN3     + " [<n>]": Key("lparen:%(n)d"),
        character.RPAREN      + " [<n>]": Key("rparen:%(n)d"),
        character.RPAREN2     + " [<n>]": Key("rparen:%(n)d"),

        ### ALPHABET
        character.A           + " [<n>]": Key("a:%(n)d"),
        character.B           + " [<n>]": Key("b:%(n)d"),
        character.C           + " [<n>]": Key("c:%(n)d"),
        character.D           + " [<n>]": Key("d:%(n)d"),
        character.E           + " [<n>]": Key("e:%(n)d"),
        character.F           + " [<n>]": Key("f:%(n)d"),
        character.G           + " [<n>]": Key("g:%(n)d"),
        character.H           + " [<n>]": Key("h:%(n)d"),
        character.I           + " [<n>]": Key("i:%(n)d"),
        character.J           + " [<n>]": Key("j:%(n)d"),
        character.K           + " [<n>]": Key("k:%(n)d"),
        character.L           + " [<n>]": Key("l:%(n)d"),
        character.M           + " [<n>]": Key("m:%(n)d"),
        character.N           + " [<n>]": Key("n:%(n)d"),
        character.O           + " [<n>]": Key("o:%(n)d"),
        character.P           + " [<n>]": Key("p:%(n)d"),
        character.Q           + " [<n>]": Key("q:%(n)d"),
        character.R           + " [<n>]": Key("r:%(n)d"),
        character.S           + " [<n>]": Key("s:%(n)d"),
        character.T           + " [<n>]": Key("t:%(n)d"),
        character.U           + " [<n>]": Key("u:%(n)d"),
        character.V           + " [<n>]": Key("v:%(n)d"),
        character.W           + " [<n>]": Key("w:%(n)d"),
        character.X           + " [<n>]": Key("x:%(n)d"),
        character.Y           + " [<n>]": Key("y:%(n)d"),
        character.Z           + " [<n>]": Key("z:%(n)d"),

        ### Numbers
        "zero": Key("0"),
        "one": Key("1"),
        "two": Key("2"),
        "three": Key("3"),
        "four": Key("4"),
        "five": Key("5"),
        "six": Key("6"),
        "seven": Key("7"),
        "eight": Key("8"),
        "nine": Key("9"),

        "numb zero": Key("0"),
        "numb one": Key("1"),
        "numb two": Key("2"),
        "numb three": Key("3"),
        "numb four": Key("4"),
        "numb five": Key("5"),
        "numb six": Key("6"),
        "numb seven": Key("7"),
        "numb eight": Key("8"),
        "numb nine": Key("9"),

        ### Function Keys
        "(F | f) one": Key("f1"),
        "(F | f) two": Key("f2"),
        "(F | f) three": Key("f3"),
        "(F | f) four": Key("f4"),
        "(F | f) five": Key("f5"),
        "(F | f) six": Key("f6"),
        "(F | f) seven": Key("f7"),
        "(F | f) eight": Key("f8"),
        "(F | f) nine": Key("f9"),
        "(F | f) ten": Key("f10"),
        "(F | f) eleven": Key("f11"),
        "(F | f) twelve": Key("f12"),

        ### Special Strings
        "(one | won) dash": Key("space, hyphen, space"),
        "line dash": Key("space, hyphen, hyphen, space"),
        "gets": Key("space, equal, space"),
        "eeks": Key("space, equal, equal, space"),
        "(not eeks | nodeeks)": Key("space, bang, equal, space"),
        "(spacebar | space bar) space": Text(" | "),
        "here (plus | add | had)": Key("space, plus, space"),
        "here minus": Key("space, hyphen, space"),
        "here times": Key("space, asterisk, space"),
        "here divide": Key("space, slash, space"),
        # "here and": Key("space, ampersand, ampersand, space"),
        "greater than": Key("space, rangle, space"),
        "greater equals": Key("space, rangle, equal, space"),
        "less than": Key("space, langle, space"),
        "less equals": Key("space, langle, equal, space"),
        "plus assign": Key("space, plus, equal, space"),
        "minus assign": Key("space, dash, equal, space"),
        "you tells": Text("utils"),

        ### Lines
        "end chuck": release + Key("s-end, del"), # del from cursor to line end
        "end copy": release + Key("s-end, c-c"), # copy from cursor to line end
        "end cut": release + Key("s-end, c-x"), # cut from cursor to line end
        "head chuck": release + Key("s-home, del"), # del from cursor to line home
        "head copy": release + Key("s-home, c-c"), # copy from cursor to line home
        "head cut": release + Key("s-home, c-x"), # cut from cursor to line home
        "wipe [<n>]": Key("end, home:2, s-down:%(n)d, del"), # del lines down
        "wipe up [<n>]": release + Key("end, home:2, s-up:%(n)d, s-home, del"), # del lines up
        "line clear": Key("end, home:2, s-end, del"), # del everything on the line except the newline
        "line copy [<n>]": release + Key("end, home:2, s-down:%(n)d, c-c, up"), # copy lines down
        "line cut [<n>]": release + Key("end, home:2, s-down:%(n)d, c-x"), # cut lines down
        "line select [<n>]": release + Key("end, home:2, s-down:%(n)d"), # select lines down
        "head select": release + Key("s-home:2"), # select from cursor to start of line
        "end select": release + Key("s-end"), # select from cursor to end of line
        "dupe": release + Key("end, home, s-end, c-c, end, enter, c-v"), # duplicate lines down

        ### words
        "bump [<n>]": release + Key("cs-right:%(n)d, del"), # del words right
        "swat [<n>]": release + Key("cs-left:%(n)d, del"), # del words left
        "scoop right [<n>]": release + Key("right:2, c-left, cs-right:%(n)d, c-c, right"), # copy words right
        "scoop left [<n>]": release + Key("left, c-right, cs-left:%(n)d, c-c, left"), # copy words left
        "slice right [<n>]": release + Key("right:2, c-left, cs-right:%(n)d, c-x, right"), # cut words right
        "slice left [<n>]": release + Key("left, c-right, cs-left:%(n)d, c-x, left"), # cut words left
        "select right [<n>]": release + Key("cs-right:%(n)d"), # select words right
        "select left [<n>]": release + Key("cs-left:%(n)d"), # select words left

        ### copy/paste
        "pace": release + Key("c-v"), # paste
        "shell pace": release + Key("cs-v"), # paste into WSL
        "pure pace": release + Key("win:down") + Key("v") + Key("win:up"), # paste without formatting
        "clone [<n>]": release + Key("c-c, c-v:%(n)d"), # copy/paste
        "copy": release + Key("c-c"), # copy
        "shell copy": release + Key("cs-c"), # copy
        "cut": release + Key("c-x"), # cut
        "tarp": release + Key("c-a"), # select all
        # "transfer": release + Key("c-a") + Key("c-x"),

        "sky <letters_ref>": Function(convert_to_upper),
        "acro <c1> <c2> [<c3>] [<c4>] [<c5>] [<c6>]": Function(acronym),
        "(Mark | mark)": Key("shift:down"),
        "(Mark | mark) up": Key("shift:up"),
        "(Mark | mark) [from] <a> [<b>] [<c>] [<d>] go <w> [<x>] [<y>] [<z>]": Function(mark_block),
        "release": release,

        ### other
        "control slap": Key("c-enter"),
        "shift slap": Key("s-enter"),
        "(bolder|boulder) [that]": Key("c-b"),
        "italics [that]": Key("c-i"),
        "undo [<n>]": Key("c-z:%(n)d"),
        "preev (window | win)": Key("a-tab/10"),
        "preev file": Key("c-tab"),
        "say <text>": release + Text("%(text)s"),
        "close tab [<n>]": Key("c-w/20:%(n)d"),
        "clean close [<n>]": Key("c-a, del, c-w/20:%(n)d"),
        "new (thing | file)": Key("c-n"),
        "file save": Key("c-s"),
        "file open": Key("c-o"),
        "it'slock": Key("capslock"),
        "etsy": Text("etc"),

        ### custom vocabulary
        "(bull | T-bull | tex bull | text bull | tex bullet | text bullet)": Text("- "),
        "CDD peptide": Text("cdd_peptide"),
    },
    extras = [
        IntegerRef("n", 1, 10000, default=1),
        # IntegerRef("m", 1, 10000, default=1),

        Integer("a", 0, 10),
        Integer("b", 0, 10),
        Integer("c", 0, 10),
        Integer("d", 0, 10),
        Integer("w", 0, 10),
        Integer("x", 0, 10),
        Integer("y", 0, 10),
        Integer("z", 0, 10),

        Dictation("text"),
        letters_reference,  # see definition of 'convert_to_upper()'
        Alternative(character.letter_number_alternatives, name="c1"),
        Alternative(character.letter_number_alternatives, name="c2"),
        Alternative(character.letter_number_alternatives, name="c3"),
        Alternative(character.letter_number_alternatives, name="c4"),
        Alternative(character.letter_number_alternatives, name="c5"),
        Alternative(character.letter_number_alternatives, name="c6"),
    ]
)
