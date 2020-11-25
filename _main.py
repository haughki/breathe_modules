import logging
logging.basicConfig()

from my_commands.imports import *

modules = {
    "my_commands": {
        "apps": [],
        "core": [
            "keys",
            "editing_commands",
        ],
        "languages": [],
    }
}

Breathe.load_modules(modules)