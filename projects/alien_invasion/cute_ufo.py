import pygame

class CuteUfo:
    """A class to manage the cute ufo."""

    def __init__(self, ai_game):
        """initializes the ufo and its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load cute ufo image and get its rect.
        self.image = pygame.image.load('images/ufo_cute.bmp')
        self.rect = self.image.get_rect()

        # Start each ufo at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ufo at it current location."""
        self.screen.blit(self.image, self.rect)