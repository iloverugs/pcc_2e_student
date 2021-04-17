import sys

import pygame

from random import randint
from star_settings import StarSettings
from star import Star


class StarrySky:
    """Overall class to manage Stars."""

    def __init__(self):
        """Initialize the assets for stars."""
        pygame.init()
        self.star_settings = StarSettings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.star_settings.screen_width = self.screen.get_rect().width
        self.star_settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()

        self._number_stars()

    def run_sky(self):
        """Start the main loop for the program."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypress."""
        if event.key == pygame.K_q:
            sys.exit()
        # elif event.key == pygame.K_r:

    def _number_stars(self):
        """Create a grid of stars."""
        # Make a star and find the number of stars in a row.
        # Spacing between each star is equal to one star width
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = (self.star_settings.screen_width
                             - (2 * star_width))
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fit on the screen.
        available_space_y = (self.star_settings.screen_height
                             - (2 * star_height))
        number_stars_y = available_space_y // (2 * star_height)

        for star_x_num in range(number_stars_y):
            for star_y_num in range(number_stars_x):
                self._check_rdm(star_x_num, star_y_num,
                                available_space_x, available_space_y)

    def _check_rdm(self, star_x_num, star_y_num,
                   available_space_x, available_space_y):
        """Checks if stars are in a grid or randomly placed."""
        if self.star_settings.star_random:
            self._create_rdm_sky(star_x_num, star_y_num,
                                 available_space_x, available_space_y)
        else:
            self._create_grid_sky(star_x_num, star_y_num)

    def _create_rdm_sky(
            self, star_x_num, star_y_num,
            available_space_x, available_space_y):
        """Create a random array of stars."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = randint(0, available_space_x)
        star.rect.x = star.x
        star.y = randint(0, available_space_y)
        star.rect.y = star.y
        self.stars.add(star)

    def _create_grid_sky(self, star_number, row_number):
        """Create an star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = (star.rect.height
                       + 2 * star.rect.height * row_number)
        self.stars.add(star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.star_settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss = StarrySky()
    ss.run_sky()
