class Settings:
    """A class to store all settings for Rocket Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 2400
        self.screen_height = 1600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.rocket_speed = 1.5