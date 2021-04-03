"""Simulates rolling dice"""
from random import randint


class Dice:
    """Simulates getting a value from an X sided die"""
    def __init__(self, dice_sides=6):
        """Initializes dice attributes"""
        self.dice_sides = dice_sides

    def roll_dice(self):
        """Simulates rolling a die"""
        roll_value = randint(1, self.dice_sides)
        print(f"I rolled a {roll_value}.")

d6_roll = Dice()
d6_roll.roll_dice()

d10_roll = Dice(10)
d10_roll.roll_dice()

d20_roll = Dice(20)
d10_roll.roll_dice()