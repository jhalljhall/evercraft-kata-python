from lib.utils.character.Alignment import Alignment
from lib.utils.character.Ability import Ability
from lib.utils.character.AbilityScore import AbilityScore



class Character:
    armor_class = 10
    hit_points = 5
    attack_power = 1
    abilities = []
    # deadness = False

    def __init__(self, name, alignment = Alignment.NEUTRAL):
        self.name = name
        self.alignment = alignment
        self.create_abilities()

    def create_abilities(self):
        for i in Ability:
            abilscore = AbilityScore(i)
            self.abilities.append(abilscore)

    @classmethod
    def set_name(self, str):
        self.name = str

    @classmethod
    def get_name(self):
        return self.name

    @classmethod
    def set_alignment(self, alignment):
        self.alignment = alignment

    @classmethod
    def get_armor_class(self):
        return self.armor_class

    @classmethod
    def get_hit_points(self):
        return self.hit_points
    
    @classmethod
    def adjust_hit_points(self, adjusted_hit_points):
        self.hit_points = adjusted_hit_points

    @classmethod
    def is_dead(self):
        if self.hit_points <= 0:
            return True      
        #     self.deadness = True
        # return self.deadness

    def get_ability(self, ability):
        for abilScore in self.abilities:
            if abilScore.ability == ability:
                return abilScore

    def get_abilityscore(self, ability):
        for abilScore in self.abilities:
            if abilScore.ability == ability:
                return abilScore.score
        #return abilities.score where abilities.ability = ability

    def get_abilitymodifier(self, ability):
        for abilScore in self.abilities:
            if abilScore.ability == ability:
                return abilScore.mod

    def set_abilityscore(self, ability, score):
        try:
            score >= 1 or score <= 20
            
        except Exception as e:
            print(e)

        else:
            for abilScore in self.abilities:
                if abilScore.ability == ability :
                    abilScore.score = score


