from lib.utils.Alignment import Alignment

class Character:
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
