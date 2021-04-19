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

    def _calculate_spacing(self):
        """Calculates the number of drops possible on the screen."""
        # Spacing between each raindrop is 1 drop width/height.
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        avail_space_x = self.rain_settings.screen_width - drop_width
        number_raindrops_x = avail_space_x // (2 * drop_width)

        # Determine the number of rows of raindrops that fit on the screen.
        avail_space_y = self.rain_settings.screen_height
        number_raindrops_y = avail_space_y // (2 * drop_height)

        return (
            avail_space_x, avail_space_y,
            number_raindrops_x, number_raindrops_y,
            drop_width, drop_height
        )

    def _create_rain(self):
        """Fill screen of raindrops."""
        r_calc = self._calculate_spacing()
        # Create the full screen of raindrops.
        for raindrop_y in range(r_calc[3]):
            self._create_raindrops_y(raindrop_y)

    def _create_raindrops_y(self, raindrop_y):
        """Create a row of raindrops."""
        r_calc = self._calculate_spacing()
        for raindrop_x in range(r_calc[2]):
            self._create_raindrop(raindrop_x, raindrop_y)

    def _create_raindrop(self, raindrop_x, raindrop_y):
        """Create a raindrop and place it in the row."""
        raindrop = Raindrop(self)
        r_calc = self._calculate_spacing()
        x_math = r_calc[4] + 2 * r_calc[4] * raindrop_x
        x_math_high = x_math + raindrop_x // 2
        x_math_low = x_math - raindrop_x // 2
        y_math_low = 2 * raindrop.rect.height * raindrop_y
        y_math_high = 2 * raindrop.rect.height * raindrop_y
        overlap_chk = raindrop
        overlap_counter = 0
        sprite_collision = pygame.sprite.spritecollideany(
                            raindrop, self.rain, collided=None
                            )

        while overlap_chk is not None:
            raindrop.x = x_math
            raindrop.y = y_math_high
            raindrop.rect.x = raindrop.x
            raindrop.rect.y = raindrop.y
            if sprite_collision is not None and overlap_counter < 30:
                overlap_counter += 1
                continue
            else:
                break

        self.rain.add(raindrop)

    def _update_rain(self):
        """
        Updates position of raindrops, and get rid of rain at the bottom.
        """
        self.rain.update()
        self._make_new_drops()

    def _make_new_drops(self):
        """Send raindrops from bttom edge to the top edge."""
        make_new_drops = False
        for raindrop in self.rain.copy():
            if raindrop.check_bottom():
                # Remove this drop
                self.rain.remove(raindrop)
                make_new_drops = True

        # Create new row of raindrops if needed.
        if make_new_drops:
            self._create_raindrops_y(0)

    def _update_screen(self):
        """Update images on teh screen, and flip to the new screen."""
        self.screen.fill(self.rain_settings.bg_color)
        self.rain.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a new game instance, and run the game.
    rd = Raindrops()
    rd.run_game()
