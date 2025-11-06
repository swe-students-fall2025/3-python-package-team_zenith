from pylloween.ghosts import draw_ghost
from pylloween.pumpkin import draw_pumpkin
from pylloween.bat import draw_bat
import random

"""
function randomly chooses which halloween symbol to draw
"""

DRAW_MAP = {1: draw_ghost, 2: draw_pumpkin, 3: draw_bat}

def draw_random(rng=random):
    """Return a random drawing as a string."""
    DRAW_MAP[random.randint(1, 3)]()

