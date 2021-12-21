#from lib.utils.character.Ability import Ability

class AbilityScore:

    def __init__(self, ability):
        self.ability = ability
        self._score = 10
        self._mod = 0

    def get_score(self):
        return self._score

    def get_mod(self):
        return self._mod
    
    def set_score(self, num):
        self._score = num
        self._mod = self.score_to_mod(num)

    score = property(get_score, set_score)

    mod = property(get_mod)
    
    def score_to_mod(self, score):
        switcher = {
            1: -5,
            2: -4,
            3: -4,
            4: -3,
            5: -3,
            6: -2,
            7: -2,
            8: -1,
            9: -1,
            10: 0,
            11: 0,
            12: 1,
            13: 1,
            14: 2,
            15: 2,
            16: 3,
            17: 3,
            18: 4,
            19: 4,
            20: 5,
        }
        return switcher.get(score)

# AbilityScore_tester = AbilityScore()

# AbilityScore_tester.score = 11

#print(AbilityScore_tester.mod)