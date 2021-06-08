class Character:
    def __init__(self, name):
        self.name = name

    @classmethod
    def set_name(self, str):
        self.name = str

    @classmethod
    def get_name(self):
        return self.name
