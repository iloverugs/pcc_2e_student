import pygame
from pygame.sprite import Sprite, Group


class Raindrop(Sprite):
    """A class to represent a single raindrop in the rain."""

    def __init__(self, r_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = r_game.screen
        self.rain_settings = r_game.rain_settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.jpg')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact vertical position.
        # self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_bottom(self):
        """Return True if alien is at bottom of the screen."""
        if self.rect.top >= self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """Move the raindrop down."""
        self.y += self.rain_settings.r_y_speed
        self.rect.y = self.y
