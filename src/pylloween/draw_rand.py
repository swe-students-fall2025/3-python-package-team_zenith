from pylloween.ghosts import draw_ghost
from pylloween.pumpkin import draw_pumpkin
from pylloween.bat import draw_bat
import random

"""
function randomly chooses which halloween symbol to draw
"""

DRAW_MAP = {1: draw_ghost, 2: draw_pumpkin, 3: draw_bat}

def draw_random(rng=random):
    """Return a random drawing as a string while still printing it."""
    if not hasattr(rng, "randint"):  # pragma: no cover - guard for misuse
        raise TypeError("rng must provide a randint(a, b) method")

    choice = rng.randint(1, len(DRAW_MAP))
    drawer = DRAW_MAP[choice]

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        result = drawer()

    art = result if isinstance(result, str) and result else buffer.getvalue()
    if not art:
        return ""

    print(art, end="" if art.endswith("\n") else "\n")
    return art
