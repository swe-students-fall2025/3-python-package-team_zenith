"""
Tests for the horrors.py
"""
import pytest
from pylloween.horrors import get_movie_idea, get_horror, short_stories, medium_stories, long_stories

# -----------------------------
# Tests for get_horror()
# -----------------------------

def test_get_horror_returns_string():
    """Should always return a string."""
    result = get_horror("short")
    assert isinstance(result, str)
    assert len(result) > 0

def test_get_horror_valid_lengths():
    """All valid lengths should return a non-empty string."""
    for length in ["short", "medium", "long"]:
        story = get_horror(length)
        assert len(story.strip()) > 0
        assert "💀" not in story  # should not return error message

def test_get_horror_invalid_length():
    """Invalid length should return an error message."""
    result = get_horror("nonsense")
    assert "invalid" in result.lower() or "choose" in result.lower()
    assert isinstance(result, str)

def test_get_horror_returns_from_correct_list():
    """Test that get_horror returns a story from the correct length list"""
    for length in ["short", "medium", "long"]:
        story = get_horror(length)
        if length == "short":
            assert story in short_stories
        elif length == "medium":
            assert story in medium_stories
        else:
            assert story in long_stories

def test_get_horror_default_parameter():
    """Test that get_horror uses 'medium' as default"""
    result = get_horror()
    assert isinstance(result, str)
    # Should be one of the medium stories
    assert result in medium_stories


# -----------------------------
# Tests for get_movie_idea()
# -----------------------------

def test_get_movie_idea_returns_string():
    """Should always return a string."""
    result = get_movie_idea("horror")
    assert isinstance(result, str)
    assert result.startswith("Genre:")

def test_get_movie_idea_valid_genres():
    """Each valid genre should include 'Genre:' and a movie title."""
    for genre in ["horror", "comedy", "cartoon", "all"]:
        movie = get_movie_idea(genre)
        assert "Genre:" in movie
        assert len(movie.splitlines()) > 1  # includes genre + movie

def test_get_movie_idea_invalid_genre():
    """Invalid genre should trigger 'not found' message."""
    result = get_movie_idea("romance")
    assert "not found" in result.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])