import logging
logging.basicConfig()

from commands.imports import *

modules = {
    "commands": {
        "apps": [],
        "core": [
            "keys",
            "editing_commands",
            "window_control",
        ],
        "languages": [],
    }
}

Breathe.load_modules(modules)