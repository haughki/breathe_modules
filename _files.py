import subprocess, os
from dragonfly import *

from supporting import utils

def openFile(command):
    subprocess.Popen(command)

def runCommand(command):
    subprocess.call(command, shell=True)

class OpenFilesRule(MappingRule):
    mapping = {
        # "file voice working": Function(openFile, command=r'notepad "C:\Users\parkeh1\Documents\voice working.txt"'),
        # "file voice working": Function(openFile, command=r'"C:\Users\parkeh1\AppData\Local\Programs\Microsoft VS Code\Code.exe" "C:\Users\parkeh1\Documents\voice working.code-workspace"'),
        # "file voice working": Function(openFile, command=r'"C:\Program Files (x86)\Nuance\NaturallySpeaking15\Program\natspeak.exe" "C:\Users\parkeh1\Documents\voice working dragon.rtf"'),
        "file pad working": Function(openFile, command=r'C:\Program Files\Windows NT\Accessories\wordpad.exe "C:\Users\parkeh1\Documents\voice working.rtf"'),
        "file random strings": Function(openFile, command=r'notepad "D:\temp\random_string.txt'),
        "file daily tasks": Function(openFile, command=r'"C:\Program Files\Windows NT\Accessories\wordpad.exe" "C:\Users\parkeh1\Documents\daily tasks.rtf"'),
        "file questions": Function(openFile, command=r'"C:\Program Files\Windows NT\Accessories\wordpad.exe" "C:\Users\parkeh1\Documents\running questions.rtf"'),

        "Evernote Linux": Function(runCommand, command=[r"C:\Users\parkeh1\Documents\evernote_links\note_linux.url"]),
        "Evernote JavaScript": Function(runCommand, command=[r"C:\Users\parkeh1\Documents\evernote_links\note_javascript.url"]),
        "Evernote Python": Function(runCommand, command=[r"C:\Users\parkeh1\Documents\evernote_links\note_python.url"]),
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