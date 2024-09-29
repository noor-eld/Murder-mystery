#######################################################################################################################
#
# CMPU 2016 OOP – TU 857 - Semester 1 Assignment.
#
# Group Project - group of 6 programmers
#
# Members:
# 1. Mohamed Benyounis (Student ID: C22394893)
# 2. Cillian Dwyer (Student ID: C22488106)
# 3. Alwalid Bouderbala (Student ID: C22793881)
# 4. Emmanuel Adeogun (Student ID: C22395881)
# 5. Noorelden Elfeky (Student ID: D22125754)
# 6. Luca Onofrei (Student ID: C22431396)
#
# Date: December 03, 2023.
#
# Game Expansion Explanation:
#
# The Game class orchestrates the entire experience, ensuring players navigate the detective adventure seamlessly.
# The game unfolds dynamically, initiating with a warm welcome, allowing players to personalize their detective
# persona before embarking on a mission to recover a missing diamond necklace. Room transitions, character interactions,
# clue investigations, and decision-making amplify the player's immersion as the master detective.
# The main features we added to the game are;
# Multiple story lines with different endings based on player decisions,
# An inventory system,
# A mini-game,
# Journal system,
# Logging/Error logging,
# Error handling.
#
# File Structure:
#
# - main_game.py: The main game script.
# - game.py: Module handling the main game events.
# - crime_scene.py: Module for managing crime scene intricacies,
#                         dealing with clues, inventory, and journals.
# - character.py: Module containing different classes each contribute different elements to the storyline.
# - loggable.py: Module used for handling logging functionality
# Running the Game:
# - To play game with our exciting expansions, run the
# "main_game.py" file.
# - Ensure that the "game.py," "crime_scene.py," loggable.py," and "character.py"
# modules are in the same directory for full functionality
#
#
# Enjoy the game :)
#
#######################################################################################################################

from game import Game

# Testing the Enhanced Game
if __name__ == "__main__":
    game = Game()
    game.run()

    # Using the logger
    print("\nGame Logs:")
    for log in game.log.logs:
        print(log)

    # Assuming game has an error_log attribute
    print("\nGame Error Logs:")
    for log in game.error_log.logs:
        print(log)
