class Character:
    name = "Ted"

    @classmethod
    def set_name(self, str):
        self.name = str

    @classmethod
    def get_name(self):
        return self.name
