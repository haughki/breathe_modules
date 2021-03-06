import logging
logging.basicConfig()

from commands.imports import *

modules = {
    "commands": {
        "apps": [
            "bash_common",
            "chrome",
            "intellij",
            "powershell",
            "vscode",
            "wsl",
        ],
        "core": [
            "aliases",
            "editing_commands",
            "example",
            "put_string_commands",
            "scan_line",
            "temp_extra",
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