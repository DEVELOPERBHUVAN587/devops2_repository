import pytest
import sys
import pygame

def pytest_configure(config):
    # Check for required dependencies before running any tests
    try:
        import pygame
        import pytest
    except ImportError as e:
        pytest.exit(f"Missing required dependency: {str(e)}")

@pytest.fixture(scope='session')
def verify_pygame():
    """Fixture to verify pygame is properly initialized"""
    try:
        pygame.init()
        pygame.mixer.init()
        yield
        pygame.quit()
    except pygame.error as e:
        pytest.fail(f"Pygame initialization failed: {str(e)}")