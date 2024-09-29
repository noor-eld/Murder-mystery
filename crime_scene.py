class CrimeScene:
    """The CrimeScene class acts as the central hub for managing crime scene intricacies,
                        dealing with clues, inventory, and journals."""

    def __init__(self, location):
        self.location = location
        self.__clues = []
        self.__investigated = False
        self.__inventory = []
        self.__journal = []
        self.__Thoughts = ""

    @property
    def investigated(self):
        return self.__investigated

    @investigated.setter
    def investigated(self, value):
        self.__investigated = value

    def add_clue(self, clue):
        self.__clues.append(clue)

    def review_clues(self):
        """At the moment there are no checks on who can see the clues. We
        might need some further protection here."""
        return self.__clues

    def add_inventory(self, item):
        self.__inventory.append(item)

    def review_inventory(self):
        return self.__inventory

    def add_biography(self, biography):
        self.__journal.append(biography)

    def review_journal(self):
        journal = [entry.replace('\\n', '\n') for entry in self.__journal]
        return journal
