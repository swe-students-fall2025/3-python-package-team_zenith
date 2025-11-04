"""
Tests for the ghost_story function from drawGhost.py module.
"""
import pytest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pylloween.drawGhost import ghost_story
from pylloween.horrors import stories


class TestGhostStory:
    """Test suite for ghost_story function"""
    
    def test_ghost_story_displays_story(self, capsys):
        """Test that ghost_story displays a horror story"""
        ghost_story("short")
        captured = capsys.readouterr()
        # Should contain speech bubble
        assert "<" in captured.out
        assert ">" in captured.out
        # Should have substantial output (story + ghost)
        assert len(captured.out) > 50
    
    def test_ghost_story_uses_correct_length(self, capsys):
        """Test that ghost_story fetches stories of correct length"""
        for length in ["short", "medium", "long"]:
            ghost_story(length)
            captured = capsys.readouterr()
            # Check that output contains a story from the correct list
            output_has_story = False
            for story in stories[length]:
                if story in captured.out:
                    output_has_story = True
                    break
            assert output_has_story, f"Should contain a {length} story"
    
    def test_ghost_story_default_medium(self, capsys):
        """Test that ghost_story uses 'medium' as default length"""
        ghost_story()
        captured = capsys.readouterr()
        # Should contain speech bubble and ghost
        assert "<" in captured.out
        assert ">" in captured.out
        assert any(char in captured.out for char in ['⣿', '⠀', '⣴', '⣰'])
    
    def test_ghost_story_includes_ghost_art(self, capsys):
        """Test that ghost_story includes the ghost ASCII art"""
        ghost_story("long")
        captured = capsys.readouterr()
        # Should have both story and ghost
        assert "<" in captured.out  # Speech bubble
        assert ">" in captured.out
        # Ghost Braille characters
        assert any(char in captured.out for char in ['⣿', '⠀', '⣴', '⣰'])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])