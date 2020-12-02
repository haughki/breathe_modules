import logging
logging.basicConfig()

from commands.imports import *

modules = {
    "commands": {
        "apps": [
            "bash_common",
            "chrome",
            "intellij",
            "vscode",
            "wsl",
        ],
        "core": [
            "editing_commands",
            "put_string_commands",
            "scan_line",
            "text_formatting",
            "window_control",
        ],
        "languages": [
            "java",
            "python",
        ],
    }
}

Breathe.load_modules(modules)