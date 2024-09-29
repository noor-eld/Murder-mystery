from abc import ABC, abstractmethod
"""The Suspect, Witness, and NPC classes each contribute different elements to the storyline"""

class Character(ABC):
    def __init__(self, name, dialogue):
        self._name = name
        self._dialogue = dialogue
        self._interacted = False

    def __str__(self):
        return f"{self.__class__.__name__}: {self._name}"

    def __eq__(self, other):
        if isinstance(other, Character):
            return self._name == other._name
        return False

    def __lt__(self, other):
        if isinstance(other, Character):
            return self._name < other._name
        return False

    def interact(self):
        if not self._interacted:
            interaction = f"{self._name}: {self._dialogue}"
            self._interacted = True
        else:
            interaction = f"{self._name} is no longer interested in talking."

        return interaction

    @property
    def dialogue(self):
        return self._dialogue

    @property
    def name(self):
        return self._name


# This class has not changed in this lab
class Suspect(Character):
    def __init__(self, name, dialogue):
        super().__init__(name, dialogue)

    def __repr__(self):
        return f"Suspect('{self._name}', '{self._dialogue}')"


class Witness(Character):
    def __init__(self, name, dialogue):
        super().__init__(name, dialogue)

    def __add__(self, other):
        if isinstance(other, Witness):
            combined_name = f"{self._name} and {other._name}"
            return Witness(combined_name)


class NPC(Character):
    """
    A class that implements the abstract class Character.
    The perform_action method must provide logic.
    The purpose of this class is to provide characters that are not
    essential for the mystery.
    """

    def interact(self):
        super().interact()
        return "\nI know nothing!"
