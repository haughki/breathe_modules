from dragonfly import Literal

SPACE       = "space"
TAB         = "punch"
S_TAB       = "funch"
ENTER       = "slap"
DEL         = "chuck"
BACKSPACE   = "back"
ESCAPE      = "fly"
AMPERSAND   = "amp"
APOSTROPHE  = "bing"
ASTERISK    = "star"
AT          = "lat"
BACKSLASH   = "chop"
BACKTICK    = "backky"
BAR         = "bar"
CARET       = "hat"
COLON       = "coal"
HYPHEN      = "dash"
COMMA       = "drip"
DOLLAR      = "doll"
DOT         = "dot"
DQUOTE      = "quote"
EQUAL       = "chud"
EXCLAMATION = "bang"
HASH        = "hash"
POUND       = "pound"
PERCENT     = "per"
PLUS        = "plus"
PRINTSCREEN = "Printscreen"
QUESTION    = "quest"
SLASH       = "slash"
SQUOTE      = "smote"
TILDE       = "till"
UNDERSCORE  = "ray"
SEMICOLON   = "Shem"
LANGLE      = "lang"
RANGLE      = "rang"
LBRACE      = "lace"
RBRACE      = "race"
LBRACKET    = "lack"
RBRACKET    = "rack"
LPAREN      = "lark"
LPAREN2     = "paren"
LPAREN3     = "el paren"
RPAREN      = "hype"
RPAREN2     = "are paren"

# A = "Alpha"
# B = "Bravo"
# C = "Charlie"
# D = "Delta"
# E = "Echo"
# F = "Foxtrot"
# G = "Gumbo"
# H = "Honda"
# I = "Igloo"
# J = "Juneau"
# K = "Kilo"
# L = "Lima"
# M = "Monty"
# N = "Ninja"
# O = "Oscar"
# P = "Papa"
# Q = "Quinn"
# R = "Robin"
# S = "Soda"
# T = "Tango"
# U = "Urdu"
# V = "Victor"
# W = "Whiskey"
# X = "X-ray"
# Y = "Yankee"
# Z = "Zulu"


A = "aim"
B = "beat"
C = "chow"
D = "drum"
E = "each"
F = "fate"
G = "gus"
H = "hip"
I = "ice"
J = "jug"
K = "Kate"
L = "lick"
M = "Mao"
N = "neat"
O = "odd"
P = "poke"
Q = "Quinn"
R = "route"
R2 = "root"
S = "suit"
T = "Tang"
U = "urge"
V = "vote"
W = "weed"
X = "decks"
Y = "yak"
Z = "zip"

letter_number_alternatives = (
	Literal(A),
	Literal(B),
	Literal(C),
	Literal(D),
	Literal(E),
	Literal(F),
	Literal(G),
	Literal(H),
	Literal(I),
	Literal(J),
	Literal(K),
	Literal(L),
	Literal(M),
	Literal(N),
	Literal(O),
	Literal(P),
	Literal(Q),
	Literal(R),
	Literal(R2),
	Literal(S),
	Literal(T),
	Literal(U),
	Literal(V),
	Literal(W),
	Literal(X),
	Literal(Y),
	Literal(Z),
	Literal("zero"),
	Literal("one"),
	Literal("two"),
	Literal("three"),
	Literal("four"),
	Literal("five"),
	Literal("six"),
	Literal("seven"),
	Literal("eight"),
	Literal("nine"),
)

character_alternatives = letter_number_alternatives + (
	Literal(SPACE),
	Literal(AMPERSAND),
	Literal(APOSTROPHE),
	Literal(ASTERISK),
	Literal(AT),
	Literal(BACKSLASH),
	Literal(BACKTICK),
	Literal(BAR),
	Literal(CARET),
	Literal(COLON),
	Literal(HYPHEN),
	Literal(COMMA),
	Literal(DOLLAR),
	Literal(DOT),
	Literal(DQUOTE),
	Literal(EQUAL),
	Literal(EXCLAMATION),
	Literal(HASH),
	Literal(POUND),
	Literal(PERCENT),
	Literal(PLUS),
	Literal(QUESTION),
	Literal(SLASH),
	Literal(SQUOTE),
	Literal(TILDE),
	Literal(UNDERSCORE),
	Literal(SEMICOLON),
	Literal(LANGLE),
	Literal(RANGLE),
	Literal(LBRACE),
	Literal(RBRACE),
	Literal(LBRACKET),
	Literal(RBRACKET),
	Literal(LPAREN),
	Literal(LPAREN2),
	Literal(LPAREN3),
	Literal(RPAREN),
	Literal(RPAREN2),
)

_base_char_map = {
	A : "a",
	B : "b",
	C : "c",
	D : "d",
	E : "e",
	F : "f",
	G : "g",
	H : "h",
	I : "i",
	J : "j",
	K : "k",
	L : "l",
	M : "m",
	N : "n",
	O : "o",
	P : "p",
	Q : "q",
	R : "r",
	R2 : "r",
	S : "s",
	T : "t",
	U : "u",
	V : "v",
	W : "w",
	X : "x",
	Y : "y",
	Z : "z",
	"zero": "0",
	"one": "1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9",
}

_punctuation_map = {
	SPACE       : " ",
	AMPERSAND   : "&",
	APOSTROPHE  : "'",
	ASTERISK    : "*",
	AT          : "@",
	BACKSLASH   : "\\",
	BACKTICK    : "`",
	BAR         : "|",
	CARET       : "^",
	COLON       : ":",
	HYPHEN      : "-",
	COMMA       : ",",
	DOLLAR      : "$",
	DOT         : ".",
	DQUOTE      : "\"",
	EQUAL       : "=",
	EXCLAMATION : "!",
	HASH        : "#",
	POUND       : "#",
	PERCENT     : "%",
	PLUS        : "+",
	QUESTION    : "?",
	SLASH       : "/",
	SQUOTE      : "'",
	TILDE       : "~",
	UNDERSCORE  : "_",
	SEMICOLON   : ";",
	LANGLE      : "<",
	RANGLE      : ">",
	LBRACE      : "{",
	RBRACE      : "}",
	LBRACKET    : "[",
	RBRACKET    : "]",
	LPAREN      : "(",
	LPAREN2     : "(",
	LPAREN3     : "(",
	RPAREN      : ")",
	RPAREN2     : ")",
}
CHARACTER_MAP = _base_char_map.copy()
CHARACTER_MAP.update(_punctuation_map)


_named_punctuation_map = {
	SPACE       : "space",
	AMPERSAND   : "ampersand",
	APOSTROPHE  : "squote",
	ASTERISK    : "askterisk",
	AT          : "at",
	BACKSLASH   : "backslash",
	BACKTICK    : "backtick",
	BAR         : "bar",
	CARET       : "caret",
	COLON       : "colon",
	HYPHEN      : "hyphen",
	COMMA       : "comma",
	DOLLAR      : "dollar",
	DOT         : "dot",
	DQUOTE      : "dquote",
	EQUAL       : "equals",
	EXCLAMATION : "exclamation",
	HASH        : "hash",
	POUND       : "hash",
	PERCENT     : "percent",
	PLUS        : "plus",
	QUESTION    : "question",
	SLASH       : "slash",
	SQUOTE      : "squote",
	TILDE       : "tilde",
	UNDERSCORE  : "underscore",
	SEMICOLON   : "semicolon",
	LANGLE      : "langle",
	RANGLE      : "rangle",
	LBRACE      : "lbrace",
	RBRACE      : "rbrace",
	LBRACKET    : "lbracket",
	RBRACKET    : "rbracket",
	LPAREN      : "lparen",
	LPAREN2     : "lparen",
	LPAREN3     : "lparen",
	RPAREN      : "rparen",
	RPAREN2     : "rparen",
}

NAMED_CHARACTER_MAP = _base_char_map.copy()
NAMED_CHARACTER_MAP.update(_named_punctuation_map)

