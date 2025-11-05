"""
pylloween package
-----------------
A spooky little Python package for Halloween fun!

This package provides:
- get_horror(length): Get a random horror story.
- get_movie_idea(genre): Get a Halloween movie suggestion.
- ghost_say(msg): Make a ghost say something.
- ghost_story(length): Make a ghost tell a story.
- ghost_idea(genre): Ghost recommends a movie.
"""

from .horrors import get_horror, get_movie_idea
from .ghosts import draw_ghost, ghost_say, ghost_story, ghost_idea
from .pumpkin import draw_pumpkin
from .treats import trick_or_treat, normalize_bag
from .bat import draw_bat
from .draw_rand import draw_random

__all__ = [
    "get_horror",
    "get_movie_idea",
    "draw_ghost",
    "ghost_say",
    "ghost_story",
    "ghost_idea",
    "draw_pumpkin",
    "trick_or_treat",
    "normalize_bag",
    "draw_bat",
    "draw_random"
]
