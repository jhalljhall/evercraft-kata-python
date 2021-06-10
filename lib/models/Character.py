from lib.utils.Alignment import Alignment

class Character:
    armor_class = 10
    hit_points = 5
    attack_power = 1
    # deadness = False

    def __init__(self, name, alignment = Alignment.NEUTRAL):
        self.name = name
        self.alignment = alignment

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
