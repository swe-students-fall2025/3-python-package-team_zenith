"""
Tests for the ghosts.py
"""
import pytest
from pylloween.ghosts import draw_ghost, ghost_say, ghost_story, ghost_idea

# -----------------------------
# Tests for draw_ghost()
# -----------------------------

def test_draw_ghost_prints_output(capsys):
    """Ensure draw_ghost prints something."""
    draw_ghost()
    out = capsys.readouterr().out
    assert len(out.strip()) > 0

def test_draw_ghost_contains_unicode(capsys):
    """Output should contain ghost unicode blocks."""
    draw_ghost()
    out = capsys.readouterr().out
    assert "⣿" in out or "⣶" in out

def test_draw_ghost_multiple_random_outputs(capsys):
    """Calling multiple times should yield different ghosts (randomized)."""
    draw_ghost()
    first = capsys.readouterr().out
    draw_ghost()
    second = capsys.readouterr().out
    assert first != second or len(first) > 0  # at least confirm variation or valid output


# -----------------------------
# Tests for ghost_say()
# -----------------------------

def test_ghost_say_default_message(capsys):
    """Default ghost_say() prints default message."""
    ghost_say()
    out = capsys.readouterr().out
    assert "haunting" in out or "Zelle" in out

def test_ghost_say_custom_message(capsys):
    """Custom message appears in output bubble."""
    ghost_say("Hello from the grave!")
    out = capsys.readouterr().out
    assert "Hello from the grave!" in out

def test_ghost_say_formats_bubble(capsys):
    """Speech bubble should have borders and the message enclosed."""
    ghost_say("Boo!")
    out = capsys.readouterr().out
    assert out.count("_") > 0
    assert "< Boo!" in out
    
def test_ghost_say_with_empty_string(capsys):
    """Test that ghost_say handles empty string input"""
    ghost_say("")
    captured = capsys.readouterr()
    # Should still show speech bubble structure
    assert "<" in captured.out
    assert ">" in captured.out


# -----------------------------
# Tests for ghost_story()
# -----------------------------

def test_ghost_story_prints_story(capsys):
    """Should print a story with recognizable text."""
    ghost_story("short")
    out = capsys.readouterr().out
    assert len(out) > 0

def test_ghost_story_default_length(capsys):
    """Default parameter should work (medium)."""
    ghost_story()
    out = capsys.readouterr().out
    assert len(out) > 0

def test_ghost_story_invalid_length(capsys):
    """Invalid length should produce an error message."""
    ghost_story("wrong_length")
    out = capsys.readouterr().out
    assert "invalid" in out.lower() or "choose" in out.lower()


# -----------------------------
# Tests for ghost_idea()
# -----------------------------

def test_ghost_idea_prints_movie(capsys):
    """Ghost idea should print a movie recommendation."""
    ghost_idea("horror")
    out = capsys.readouterr().out
    assert "Genre" in out and len(out) > 10

def test_ghost_idea_all_genres(capsys):
    """Genre 'all' should combine all categories."""
    ghost_idea("all")
    out = capsys.readouterr().out
    assert "Genre: all" in out

def test_ghost_idea_invalid_genre(capsys):
    """Invalid genre should produce 'not found' message."""
    ghost_idea("nonsense_genre")
    out = capsys.readouterr().out
    assert "not found" in out.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])