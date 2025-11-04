"""
Tests for the draw_ghost function from drawGhost.py module.
"""
import pytest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pylloween.drawGhost import draw_ghost, GHOST_STYLES


class TestDrawGhost:
    """Test suite for draw_ghost function"""
    
    def test_draw_ghost_prints_output(self, capsys):
        """Test that draw_ghost prints something to stdout"""
        draw_ghost()
        captured = capsys.readouterr()
        assert len(captured.out) > 0
        # Check that it contains some ghost-like Braille characters
        assert '⣿' in captured.out or '⠀' in captured.out or '⣴' in captured.out
    
    def test_draw_ghost_prints_valid_style(self, capsys):
        """Test that draw_ghost prints one of the valid ghost styles"""
        draw_ghost()
        captured = capsys.readouterr()
        # Output should match one of the ghost styles
        output_found = False
        for style in GHOST_STYLES.values():
            if style.strip() in captured.out.strip():
                output_found = True
                break
        assert output_found, "Output should match one of the predefined ghost styles"
    
    def test_draw_ghost_consistent_multiple_calls(self, capsys):
        """Test that draw_ghost produces output on multiple calls"""
        for _ in range(3):
            draw_ghost()
            captured = capsys.readouterr()
            assert len(captured.out) > 0
            # Should contain ghost characters
            assert any(char in captured.out for char in ['⣿', '⠀', '⣴', '⣰'])

    def test_draw_ghost_specific_style(self, capsys):
        """Test that specifying a style prints that exact ghost"""
        draw_ghost(1)
        captured = capsys.readouterr()
        assert GHOST_STYLES[1].strip() in captured.out.strip()

        draw_ghost("2")
        captured = capsys.readouterr()
        assert GHOST_STYLES[2].strip() in captured.out.strip()

    def test_draw_ghost_invalid_style(self):
        """Test that invalid style inputs raise an error"""
        with pytest.raises(ValueError):
            draw_ghost(99)
        with pytest.raises(ValueError):
            draw_ghost("ghosty")
        with pytest.raises(TypeError):
            draw_ghost(3.14)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
