class RSettings:
    """A class to store all settings for Raindrops."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 2400
        self.screen_height = 1600
        self.bg_color = (0, 0, 0)

        # Raindrop settings
        self.r_y_speed = 10
