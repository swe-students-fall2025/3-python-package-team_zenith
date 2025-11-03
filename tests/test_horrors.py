"""
Tests for the horrors.py module (get_horror function).
"""
import pytest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pylloween.horrors import get_horror, stories


class TestGetHorror:
    """Test suite for get_horror function"""
    
    def test_get_horror_returns_string(self):
        """Test that get_horror returns a string"""
        result = get_horror("short")
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_get_horror_valid_lengths(self):
        """Test that get_horror works with all valid length parameters"""
        for length in ["short", "medium", "long"]:
            result = get_horror(length)
            assert isinstance(result, str)
            assert len(result) > 0
    
    def test_get_horror_invalid_length(self):
        """Test that get_horror returns error message for invalid length"""
        result = get_horror("invalid")
        assert "invalid parameter" in result.lower()
        assert isinstance(result, str)
    
    def test_get_horror_returns_from_correct_list(self):
        """Test that get_horror returns a story from the correct length list"""
        result = get_horror("short")
        # Should be one of the short stories
        assert any(story == result or result in story for story in stories["short"])
    
    def test_get_horror_default_parameter(self):
        """Test that get_horror uses 'medium' as default"""
        result = get_horror()
        assert isinstance(result, str)
        # Should be one of the medium stories
        assert any(story == result or result in story for story in stories["medium"])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])