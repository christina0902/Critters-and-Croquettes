from datetime import date


class LLama:
    def __init__(self, name, species, shfift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"
