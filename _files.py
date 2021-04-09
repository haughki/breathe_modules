import subprocess
from dragonfly import *

from supporting import utils

def openFile(command):
    subprocess.Popen(command)

class OpenFilesRule(MappingRule):
    mapping = {
        "file voice working": Function(openFile, command=r'notepad "C:\Users\parkeh1\Documents\voice_working.txt"'),
        "file random strings": Function(openFile, command=r'notepad "D:\temp\random_string.txt'),
        "file daily tasks": Function(openFile, command=r'"C:\Program Files\Windows NT\Accessories\wordpad.exe" "C:\Users\parkeh1\Documents\daily tasks.rtf"'),
        "file questions": Function(openFile, command=r'"C:\Program Files\Windows NT\Accessories\wordpad.exe" "C:\Users\parkeh1\Documents\running questions.rtf"'),
    }
    extras = [Dictation("text"),
              ]
    defaults = {"text":None}


open_files_grammar = Grammar("Open certain files")
open_files_grammar.add_rule(OpenFilesRule())


open_files_grammar.load()

def unload():
    global open_files_grammar
    open_files_grammar = utils.unloadHelper(open_files_grammar, __name__)