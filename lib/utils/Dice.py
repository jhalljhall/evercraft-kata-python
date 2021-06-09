class Dice:

    dice_roll_result = 0

    def __init__(self, num):
        self.dice_roll_result = num

    def roll(self):
        return self.dice_roll_result