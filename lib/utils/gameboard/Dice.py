from lib.utils.gameboard.DiceType import DiceType

class Dice:
    dicetype = 0
    dice_roll_result = 0
    isCritical = False

    def __init__(self, num, dicetype = DiceType.TWENTY):
        self.dice_roll_result = num
        self.dicetype = self.dicetype

    def roll(self):
        if self.dice_roll_result == self.dicetype:
            self.isCritical = True
        return self.dice_roll_result
