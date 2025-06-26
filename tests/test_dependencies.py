import pytest
import importlib

# List of required dependencies
REQUIRED_DEPENDENCIES = [
    ('pygame', '2.0.0'),
    ('pytest', '7.0.0'),
]


@pytest.mark.parametrize("package_name,min_version", REQUIRED_DEPENDENCIES)
def test_dependency_versions(package_name, min_version):
    """Test that required dependencies are installed with minimum versions"""
    try:
        module = importlib.import_module(package_name)
        installed_version = getattr(module, '__version__', '0.0.0')

        # Split version strings into comparable parts
        min_parts = list(map(int, min_version.split('.')))
        installed_parts = list(map(int, installed_version.split('.')[0:3]))  # Take first 3 parts

        assert installed_parts >= min_parts, \
            f"{package_name} version {installed_version} is less than required {min_version}"

    except ImportError:
        pytest.fail(f"{package_name} is not installed")


def test_pygame_modules_available():
    """Test that specific pygame modules are available"""
    import pygame
    assert hasattr(pygame, 'mixer'), "pygame.mixer module not available"
    assert hasattr(pygame, 'font'), "pygame.font module not available"
    assert hasattr(pygame, 'display'), "pygame.display module not available"

    import os

    def test_sound_files_exist():
        """Test that required sound files exist"""
        required_files = [
            'correct.wav',
            'incorrect.wav',
            'background_music.mp3'
        ]

        missing_files = [f for f in required_files if not os.path.exists(f)]
        assert not missing_files, f"Missing sound files: {', '.join(missing_files)}"

    def test_sound_files_are_accessible():
        """Test that sound files can be loaded"""
        import pygame
        pygame.mixer.init()

        test_files = [
            ('correct.wav', pygame.mixer.Sound),
            ('incorrect.wav', pygame.mixer.Sound),
            ('background_music.mp3', pygame.mixer.music)
        ]

        for filename, loader in test_files:
            try:
                if loader == pygame.mixer.music:
                    loader.load(filename)
                else:
                    loader(filename)
            except pygame.error as e:
                pytest.fail(f"Failed to load {filename}: {str(e)}")
            finally:
                if loader == pygame.mixer.music:
                    pygame.mixer.music.stop()