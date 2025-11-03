"""
Tests for the ghost_say function from drawGhost.py module.
"""
import pytest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pylloween.drawGhost import ghost_say


class TestGhostSay:
    """Test suite for ghost_say function"""
    
    def test_ghost_say_with_custom_message(self, capsys):
        """Test that ghost_say displays the custom message"""
        test_message = "Boo! I am a test ghost!"
        ghost_say(test_message)
        captured = capsys.readouterr()
        assert test_message in captured.out
        # Should have speech bubble borders
        assert "<" in captured.out
        assert ">" in captured.out
    
    def test_ghost_say_default_message(self, capsys):
        """Test that ghost_say uses default message when none provided"""
        ghost_say()
        captured = capsys.readouterr()
        # Should contain the default warning message
        assert "haunting" in captured.out or "terminal" in captured.out
        assert "<" in captured.out
        assert ">" in captured.out
    
    def test_ghost_say_includes_ghost_drawing(self, capsys):
        """Test that ghost_say includes the ghost ASCII art"""
        ghost_say("Test message")
        captured = capsys.readouterr()
        # Should contain both speech bubble and ghost art
        assert "<" in captured.out
        assert ">" in captured.out
        # Ghost art uses Braille characters
        assert any(char in captured.out for char in ['⣿', '⠀', '⣴', '⣰'])
    
    def test_ghost_say_with_empty_string(self, capsys):
        """Test that ghost_say handles empty string input"""
        ghost_say("")
        captured = capsys.readouterr()
        # Should still show speech bubble structure
        assert "<" in captured.out
        assert ">" in captured.out


if __name__ == "__main__":
    pytest.main([__file__, "-v"])