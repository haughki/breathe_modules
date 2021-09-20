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
            "moba_x_term",
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
            "javascript",
        ],
    }
}

Breathe.load_modules(modules)