import pytest

from pylloween.pumpkin import draw_pumpkin
from pylloween.bat import draw_bat
from pylloween.draw_rand import draw_random

'''
test for drawing pumpkin
'''

def test_draw_pumpkin_returns_string():
    """Function should return a non-empty string."""
    art = draw_pumpkin()
    assert isinstance(art, str)
    assert len(art.strip()) > 0

def test_draw_pumpkin_contains_key_glyphs():
    """Returned string should contain expected ASCII/Unicode bits."""
    art = draw_pumpkin()
    assert "___" in art
    assert "''---.....--''" in art or "''-.,_______,.-*'" in art or ".__" in art

'''
test for drawing bat
'''

def test_draw_bat_returns_string():
    """Function should return a non-empty string."""
    art = draw_bat()
    assert isinstance(art, str)
    assert len(art.strip()) > 0

def test_draw_bat_contains_key_glyphs():
    """Returned string should contain expected ASCII/Unicode bits."""
    art = draw_bat()
    assert "/-\\/-\\".replace("\\", "\\\\") 
    assert "/" in art and "\\" in art and "^" in art

"""
test for random drawing function
"""

def test_draw_random_pumpkin(monkeypatch, capsys):
    """When RNG yields 1, pumpkin art is printed."""
    monkeypatch.setattr(draw_random, "randint", lambda a, b: 1)
    draw_random()
    out = capsys.readouterr().out
    assert "___" in out  # pumpkin token

def test_draw_random_bat(monkeypatch, capsys):
    """When RNG yields 2, bat art is printed."""
    monkeypatch.setattr(draw_random, "randint", lambda a, b: 2)
    draw_random()
    out = capsys.readouterr().out
    assert "^" in out and "\\" in out  # bat tokens

def test_draw_random_ghost(monkeypatch, capsys):
    """When RNG yields 3, ghost art is printed."""
    monkeypatch.setattr(draw_random, "randint", lambda a, b: 3)
    draw_random()
    out = capsys.readouterr().out
    # pick a distinctive ghost char from your ghost output
    assert "⣿" in out or "⣴⣿" in out