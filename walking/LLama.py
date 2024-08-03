class LLama:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

    def __str__(self):
        return f"{self.name} is a {self.species}"