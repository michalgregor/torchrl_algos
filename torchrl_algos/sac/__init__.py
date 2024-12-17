import os
from .sac import main

def get_config_path():
    return os.path.join(os.path.dirname(__file__))