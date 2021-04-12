import sys

import pygame

from star_settings import StarSettings

class Stars:
    """Overall class to manage Stars."""

    def __init__(self):
        """Initialize the assets for stars."""
        pygame.init()
        self.star_settings = StarSettings()
        