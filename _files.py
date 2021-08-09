import subprocess, os
from dragonfly import *

from supporting import utils

def openFile(command):
    subprocess.Popen(command)

def runCommand(command):
    subprocess.call(command, shell=True)

class OpenFilesRule(MappingRule):
    mapping = {
        "file voice working": Function(openFile, command=r'notepad "G:\My Drive\voice working.txt"'),
        # "file voice working": Function(openFile, command=r'"C:\Users\parkeh1\AppData\Local\Programs\Microsoft VS Code\Code.exe" "G:\My Drive\voice working.code-workspace"'),
        #"file pad working": Function(openFile, command=r'C:\Program Files\Windows NT\Accessories\wordpad.exe "G:\My Drive\voice working.rtf"'),
        "file random strings": Function(openFile, command=r'notepad "D:\temp\random_string.txt'),
        "file daily tasks": Function(openFile, command=r'"C:\Program Files\Windows NT\Accessories\wordpad.exe" "G:\My Drive\daily tasks.rtf"'),
        "file [running] questions": Function(openFile, command=r'"C:\Program Files\Windows NT\Accessories\wordpad.exe" "G:\My Drive\running questions.rtf"'),

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