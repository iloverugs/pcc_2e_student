import sys

import pygame

class EmptyScreen:
    """Uses pygame to create an empty screen, and detects KEY_DOWN."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Empty Screen")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            pygame.display.flip()

    def _check_events(self):
        """Respond to keypress events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    es = EmptyScreen()
    es.run_game()
