import sys

import pygame

from rain_settings import RSettings
from raindrop import Raindrop
from random import randint


class Raindrops:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.rain_settings = RSettings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.rain_settings.screen_width = self.screen.get_rect().width
        self.rain_settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Raindrops")

        self.rain = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_rain()
            self._update_screen()

    def _check_events(self):
        """Respond to kepresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _update_rain(self):
        """
        Updates position of raindrops, and get rid of rain at the bottom.
        """
        self._check_bottom_edge()
        self.rain.update()

    def _calculate_spacing(self):
        """Calculates the number of drops possible on the screen."""
        # Spacing between each raindrop is 1 drop width/height.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        avail_space_x = self.rain_settings.screen_width - (2 * raindrop_width)
        number_raindrops_x = avail_space_x // (2 * raindrop_width)

        # Determine the number of rows of raindrops that fit on the screen.
        avail_space_y = self.rain_settings.screen_height - (2 * raindrop_height)
        number_raindrops_y = avail_space_y // (2 * raindrop_height)

        return (
            avail_space_x, avail_space_y,
            number_raindrops_x, number_raindrops_y,
            raindrop_width, raindrop_height
        )

    def _create_rain(self):
        """Fill screen of raindrops."""
        r_calc = self._calculate_spacing()
        # Create the full screen of raindrops.
        for raindrop_y in range(r_calc[3]):
            print(raindrop_y)
            for raindrop_x in range(r_calc[2]):
                self._create_raindrop(raindrop_x, raindrop_y)

    def _create_raindrop(self, raindrop_x, raindrop_y):
        """Create a raindrop and place it in the row."""
        raindrop = Raindrop(self)
        r_calc = self._calculate_spacing()
        x_math_high = r_calc[4] + 2 * r_calc[4] * raindrop_x
        y_math_low = 2 * raindrop.rect.height * raindrop_y
        y_math_high = raindrop.rect.height \
                      + 2 * raindrop.rect.height * raindrop_y
        overlap_chk = raindrop
        overlap_counter = 0

        raindrop.x = x_math_high
        raindrop.y = y_math_high
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop.y

        self.rain.add(raindrop)

    def _check_bottom_edge(self):
        """Send raindrops from bttom edge to the top edge."""
        for raindrop in self.rain.sprites():
            if raindrop.check_bottom():
                self.rain.remove(raindrop)

                # Create new row of rain
                r_calc = self._calculate_spacing()
                for raindrop_x in range(r_calc[2]):
                    self._create_raindrop(raindrop_x, 0)
                break

    def _update_screen(self):
        """Update images on teh screen, and flip to the new screen."""
        self.screen.fill(self.rain_settings.bg_color)
        self.rain.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a new game instance, and run the game.
    rd = Raindrops()
    rd.run_game()
