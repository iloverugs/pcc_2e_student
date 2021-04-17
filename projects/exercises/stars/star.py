import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent an individual star in the grid."""

    def __init__(self, starry_sky):
        """Initialize the star and its location."""
        super().__init__()
        self.screen = starry_sky.screen

        # Load the star image and set its rect attributes
        self.image = pygame.image.load('images/star.jpg')
        self.rect = self.image.get_rect()

        # Put first star near top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
