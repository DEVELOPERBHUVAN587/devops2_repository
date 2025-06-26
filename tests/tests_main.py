import pytest
from unittest.mock import MagicMock, patch, mock_open
import pygame
import sys
import importlib
from importlib import reload


# Mock the sound files before importing main
@pytest.fixture(autouse=True, scope="module")
def mock_sound_files():
    with patch('pygame.mixer.Sound', MagicMock()), \
            patch('pygame.mixer.music.load', MagicMock()):
        # Now import main after mocks are in place
        global main
        import main
        yield
        # Cleanup
        if 'main' in sys.modules:
            del sys.modules['main']


@pytest.fixture(autouse=True)
def mock_pygame(monkeypatch):
    """Mock Pygame functions to allow testing without a display"""
    # Mock pygame initialization
    monkeypatch.setattr(pygame, 'init', MagicMock())
    monkeypatch.setattr(pygame.mixer, 'init', MagicMock())

    # Mock display functions
    monkeypatch.setattr(pygame.display, 'set_mode', MagicMock(return_value=MagicMock()))
    monkeypatch.setattr(pygame.display, 'set_caption', MagicMock())
    monkeypatch.setattr(pygame.display, 'flip', MagicMock())

    # Mock font rendering
    mock_font = MagicMock()
    mock_font.render.return_value = MagicMock()
    mock_font.size.return_value = (10, 10)
    monkeypatch.setattr(pygame.font, 'Font', MagicMock(return_value=mock_font))

    # Mock time functions
    monkeypatch.setattr('time.sleep', MagicMock())


# Rest of your test functions remain the same...
def test_add_line_breaks():
    """Test the line breaking functionality"""
    long_text = "a" * 150
    broken_text = main.add_line_breaks(long_text, 100)
    assert len(broken_text.split('\n')) == 2
    assert broken_text.count('\n') == 1

    # Test with exact line length
    exact_line = "a" * 100
    broken_exact = main.add_line_breaks(exact_line, 100)
    assert len(broken_exact.split('\n')) == 1

    # Test with empty string
    assert main.add_line_breaks("", 100) == ""

# ... rest of your test functions ...