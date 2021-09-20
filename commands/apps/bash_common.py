from commands.imports import *
from supporting import utils


# def T(s, pause=0.00001, **kws):
#     return Text(s, pause=pause, **kws)

def T(s, **kws):
    return Text(s, **kws)

def K(*args, **kws):
    return Key(*args, **kws)

def P(*args, **kws):
    return Pause(*args, **kws)

def M(*args, **kws):
    return Mouse(*args, **kws)

def printUpDir(w=1):
    cd_command = "cd "
    for i in range(w):
        cd_command += "../"
    Text(cd_command).execute()
    Key("enter").execute()

Breathe.add_commands(
    # mintty is git bash, git for Windows
    context=AppContext(executable='ubuntu') | AppContext(executable='MobaXterm') | AppContext(executable='mintty') | AppContext(executable='WindowsTerminal'),
    mapping = {
        # directories
        "direct home": Text("cd ~") + Key("enter"),
        "direct temp": T("cd ~/temp") + K("enter"),

        "apt get clean": T("apt-get clean"),
        "apt get install": T("apt-get install "),
        "apt get update": T("apt-get update"),
        "apt get upgrade": T("apt-get upgrade"),
        "clear arg [<n>]": Key("c-w:%(n)d"),
        "arg swat [<n>]": Key("c-w:%(n)d"),
        "clear line": Key("c-a") + Key("c-k"),
        "control break": K("c-c"),
        "cat": T("cat "),
        # "Clyde copy": T("cp "),
        "do copy": T("cp "),
        "do copy recursive": T("cp -r "),
        "chai": T("cd "),
        "chai <text>": T("cd %(text)s") + K("tab,enter"),
        "chai chain <text>": T("cd %(text)s") + K("tab:3"),
        "chain <text>": T("%(text)s") + K("tab:3"),
        "chai up [<w>]": Function(printUpDir),  # + Key("enter")
        # "chaif <common_folder>": T("cd %(common_folder)s\n"),
        "echo": T("echo "),
        # "echo path": T("echo $PATH\n"),
        "environment": T("env\n"),
        # "<grep>": T("%(grep)s -rin -B2 -A2 '' .") + K("left:3"),
        # "<grep> <text>": T("%(grep)s -rin -B2 -A2 '%(text)s' .\n"),
        "grep": T("grep "),
        "grep long": T("grep -rin -B2 -A2 '' .") + K("left:3"),
        "grep <text>": T("grep -rin -B2 -A2 '%(text)s' .\n"),
        "info documentation": T("info "),
        "jobs": T("jobs -l\n"),
        "jobs running": T("jobs -lr\n"),
        "jobs stopped": T("jobs -ls\n"),
        "less": T("less "),
        "list": T("LC_COLLATE=C ls -AlF\n"),
        "list short": Text("ls") + Key("enter"),
        "list filter": T("ls -al | grep "),
        "list <text>": T("ls -al %(text)s") + K("tab,enter"),
        "list chain <text>": T("ls -al %(text)s") + K("tab:3"),
        "list up": T("ls -al ..\n"),
        "list up up": T("ls -al ../..\n"),
        "locate": T("locate "),
        "man page": T("man "),
        "make directory": T("mkdir "),
        "make directory <text>": T("mkdir %(text)s\n"),
        "make directory parent": T("mkdir -p "),
        "make directory parent <text>": T("mkdir -p %(text)s\n"),
        "move": T("mv "),
        "move <text>": T("mv %(text)s"),
        "move <text> to [<text2>]": T("mv %(text)s") + K("tab") + T(" %(text2)s") + K("tab"),
        "processes": T("ps aux\n"),
        "process grep": T('ps aux | egrep "PID|"') + K("left"),
        "push (directory | chai)": T("pushd .\n"),
        "push other (directory | chai)": T("pushd "),
        "pop (directory | chai)": T("popd\n"),
        "(directory | chai) stack": T("dirs\n"),
        "print (working directory | chai)": T("pwd\n"),
        "remove": T("rm "),
        "remove directory": T("rmdir "),
        "remove directory recursively": T("rmdir -r"),
        "run": T("./"),
        "run <text>": T("./%(text)s") + K("tab,enter"),
        "super do": T("sudo "),
        "switch user": T("su "),
        "time": T("time "),
        "trash": T("trash "),
        "who am I": T("whoami\n"),
        "help flag": T(" --help"),
        "help flag short": T(" -h"),
        "verbose flag": T(" --verbose"),
        "verbose flag short": T(" -v"),

        # tools
        "Conda": T("conda "),
        "get ": T("git "),
        "get status": T("git status") + K("enter"),
        "NPM": T("npm "),
        "pip three install": T("pip3 install "),
        "pip three uninstall": T("pip3 uninstall "),
        "to Jason": Text(" | python -m json.tool") + Key("enter"),
        "vim": T("vim "),
        "vim <text>": T("vim %(text)s") + K("tab,enter"),
        "suvim": T("sudo vim "),
        "suvim <text>": T("sudo vim %(text)s") + K("tab,enter"),
        "web get": T("wget "),

    },

    extras = [
        Integer("t", 1, 50),
        Dictation("text"),
        Dictation("text2"),
        IntegerRef("n", 1, 50000),
        Integer("w", 1, 10),
        # Integer("x", 0, 10),
        # Integer("y", 0, 10),
        # Integer("z", 0, 10)
    ],
    defaults = {
        "t": 1,
        "n": 1,
        "text": "",
        "text2": ""
    }
)

