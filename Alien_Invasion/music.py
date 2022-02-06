import pygame.mixer


class Music:
    """A class to store music."""

    def __init__(self, ai_game):
        """Initialize music and sound attributes."""
        self.BGM = pygame.mixer.music.load('music/background_music.mp3')
