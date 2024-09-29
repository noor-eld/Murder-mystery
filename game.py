# CMPU-2016 Object-Oriented Programming
# TU857-2
#
# The Game class orchestrates the entire experience, ensuring players navigate the detective adventure seamlessly.
# The game unfolds dynamically, initiating with a warm welcome, allowing players to personalize their detective
# persona before embarking on a mission to recover a missing diamond necklace. Room transitions, character interactions,
# clue investigations, and decision-making amplify the player's immersion as the master detective.

from loggable import Loggable
from character import Suspect, Witness, NPC
from crime_scene import CrimeScene
import random


class Game:
    def __init__(self):
        # Initialize the game with different characters and settings
        self.__crime_scene = CrimeScene("mrs. hootch's Mansion")
        self.__logger = Loggable()

        # A second logger that is specific to any error logs
        self.__error_logger = Loggable()

        # Game state variables:
        self.__running = True
        self.__game_started = False

        # Suspect information
        self.__suspect1_information = ("name: Sam Everton \nAge: 26 \nheight: 5'10 \nmore info: loves talking about "
                                       "biology,and likes Samantha Evans\n")
        self.__suspect2_information = ("name: Samantha Evans \nAge: 25 \nheight: 5'8 \nmore info: Likes having an "
                                       "bragging on expensive things\n")
        self.__suspect3_information = ("name: Josh Burn \nAge: 31 \nheight: 6'1 \nmore info: Always loses things, "
                                       "likes to be alone sometimes\n")

        # Initialize characters
        self.__suspect1 = Suspect("Sam Everton:", "Oh umm.. its you, biology is a fascinating subject, "
                                                  "it says here that DNA, the blueprint of life, is coiled and packed"
                                                  " into the nucleus of each human cell, and if stretched out, it would"
                                                  " reach over six feet in length! On the next page... oh ye i forgot"
                                                  " i ripped it out cuz it had a password for something... "
                                                  "isn't Samantha so beautiful?")
        self.__suspect2 = Suspect("Samantha Evans:", "Oh hi your the detective right? Im telling you its"
                                                     " not me. But look at this Expensive leopard fur jacket I got"
                                                     "Its sooo confy,i bet its like 10k at least, i LOVE expensive "
                                                     "things I found this note saying its from a secret admirer, I "
                                                     "wonder who it is, it does have a missing patch but nobody can "
                                                     "notice because of the fur.")
        self.__suspect3 = Suspect("Josh Burn:", "OMG I CAN'T FIND IT, oh hello detective, have you seen "
                                                "My ID card?, I need it to open something")

        self.__witness1 = Witness("John smith:", "Yo mr detective, I've got a game for you "
                                                 "Not interested? ill give you information on all 3 suspects "
                                                 "If you play")
        self.__witness2 = Witness("Maid:", "I was cleaning and i noticed fingerprints on the safe "
                                           "combination specifically the numbers 3, 6 and 7.")
        self.__npc1 = NPC("Butler:", "Your the detective right? "
                                     "Thank god your here, this diamond necklace means a lot to mrs.hooch "
                                     "You should probably check upstairs first. ")
        self.__npc_ghost1 = NPC("Sir Reginald Greythorne: ", "Before you pick a door, i shall give you "
                                                             "advice, there are 3 Mystery doors, one healthy and "
                                                             "\nothers deadly numbered from 1-3, i shall give you a "
                                                             "clue on which one you shall see.But if you get it wrong "
                                                             "\nthere will by no return here is the clue for "
                                                             "the right number: "
                                                             "\nI'm the smallest prime, yet not alone, "
                                                             " Even and elusive, in math I'm known. What am I, "
                                                             "in a numerical tone?"
                                                             "\n interesting.. the answer to this riddle could be of "
                                                             "help in the future.")
        self.__npc_ghost2 = NPC("Lady Seraphina Holloway:"
                                , "Between one of these doors, is the answer your looking,"
                                  "The number to enter is the loneliest one,standing alone"
                                  "in a game of addition its easily known "
                                  "neither prime nor even, a unique identity")
        self.__npc2 = NPC("Mo:", "I'M INNOCENT PLEASE DON'T HIT ME!!")
        self.__npc3 = NPC("mrs. Hooch:", "Good Evening detective, have you found the culprit yet?")

        # Game variables
        self.current_room = "lobby"
        self.__clues = []
        self.__trigger_ghost1 = False
        self.__trigger_meeting_room = False
        self.__trigger_ghost2 = False
        self.__knife = False
        self.__IDcard = False
        self.__kitchen_key = False
        self.__interact_witness1 = False
        self.__interact_witness2 = False
        self.__interact_suspect1 = False
        self.__interact_suspect2 = False
        self.__interact_suspect3 = False
        self.__safe_opened = False

    # ---
    # property methods first
    # ---

    @property
    def log(self):
        return self.__logger

    @property
    def error_log(self):
        return self.__error_logger

    def run(self):
        # Main game loop
        self.__logger.log("Game started")
        print("***********************************************************************************")
        print("Welcome to 'The Poirot Mystery'")
        print("You are about to embark on a thrilling adventure as a detective.")
        print("Your expertise is needed to solve a complex case and unveil the truth.")
        print("***********************************************************************************")
        while self.__running:
            try:
                self.update()
            except ValueError as ve:
                # Error handling for ValueError
                self.__error_logger.log(f"Error found:\n {ve}.")
            except Exception:
                # General error handling
                self.__error_logger.log("Unexpected error from run():\n{e}.")
                print("Unexpected caught error during running of the Game. "
                      "We continue playing...")
            else:
                # Log successful update
                self.__logger.log("Successfully updating")
            finally:
                # Always log message at end of each loop
                self.__logger.log("---")

    def update(self):
        # Game update method handling input and game state
        self.__logger.log("I'm updating")
        # Implementation details

        if not self.__game_started:
            # Start game with initial setup and introduction
            player_input = input("Press 'q' to quit or 's' to start: ")
            try:
                # Error handling block
                if player_input.lower() == "q":
                    # Stops game if player quits
                    self.__running = False
                elif player_input.lower() == "s":
                    self.__game_started = True
                    self.start_game()
                else:
                    raise ValueError(f"{player_input}")
            except ValueError as e:
                # Handles the error incorrect input and prompts again
                print(f"Please choose between q and s.")
                self.__error_logger.log(f"Wrong value entered: {e}")
            except Exception as ve:
                # Catches any unexpected errors during game start
                print(f"Unexpected error occurred.")
                self.__error_logger.log(f"Unexpected Error: {ve}")
            self.__logger.log(f"Player input: {player_input}")

        else:
            # Handles game interaction after game has started

            player_input = input(
                "----------------------------------------------------------------\n"
                "Press 'q' to quit, 'i' to interact with characters in the room, "
                "'e' to examine clues, 'r' to review clues, \n 'b' to review inventory, "
                "'j' to review your journal or 'd' to choose an available door/path to go through: \n"
                "----------------------------------------------------------------\n")
            try:
                if player_input.lower() == "q":
                    self.__running = False
                    self.log.save_logs_on_exit()
                    self.__logger.log("Quit the game")
                elif player_input.lower() == "i":
                    self.interact_with_characters()
                elif player_input.lower() == "e":
                    self.examine_room()
                elif player_input.lower() == "d":
                    self.choose_door()
                elif player_input.lower() == "r":
                    clues = self.__crime_scene.review_clues()
                    if clues:
                        print(clues)
                    else:
                        print("You have not found any clues yet.")
                elif player_input.lower() == "b":
                    items = self.__crime_scene.review_inventory()
                    if items:
                        print(items)
                    else:
                        print("Inventory is empty.")
                elif player_input.lower() == "j":
                    biography = self.__crime_scene.review_journal()
                    self.__logger.log("Reviewed Journal")
                    if biography:
                        for biography in self.__crime_scene.review_journal():
                            print(biography)
                    else:
                        print("journal is empty.\n "
                              "Tip: To fill the journal you will need to play the "
                              "minigame with the Witness in the lobby\n")
                else:
                    raise ValueError(f"{player_input}")
            except ValueError as e:
                # Handles incorrect input with a prompt to choose a correct option
                print(f"Please choose from the options provided.")
                self.__error_logger.log(f"Wrong value entered: {e}")
            except Exception as ve:
                # Handles any unexpected errors during gameplay
                print(f"Unexpected error occurred.")
                self.__error_logger.log(f"Unexpected Error: {ve}")

            self.__logger.log(f"Player input: {player_input}")

    def start_game(self):
        # Logs beginning of game start
        self.__logger.log("Game is starting")

        # prompts the player to enter the name of their character
        player_name = input("Enter your detective's name: ")
        print(f"Welcome, Detective {player_name}!")
        print("You enter the dimly lit mansion lobby, flanked by an anxious-looking man"
              " and the witness.")
        print("As the famous detective, you're here to solve the mysterious case of...")
        print("'The Missing Diamond Necklace'.")
        print("Put your detective skills to the test and unveil the truth!")
        print("mrs. Hootch, the owner of the mansion, has equipt you with a jornal to fill the possible suspects, "
              "witnesses and others with")

    def interact_with_characters(self):
        """The interact_with_characters method within the Game class
        demonstrates the interaction with characters. """

        # Method to handle interaction with character based on choice
        self.__logger.log("Interactions happening: ")

        print("\nYou decide to interact with the characters in the room.")

        # Handles interactions in the lobby
        if self.current_room == "lobby":
            while True:
                try:
                    # Error handling block
                    character = int(input("\nIf you want to speak to the witness "
                                          "choose 1: \nIf you'd like to speak to the Butler "
                                          "choose 2: "
                                          "\nIf you'd like to exit from this menu "
                                          "choose 3: "))
                    if character == 1:
                        if not self.__interact_witness1:
                            print(self.__witness1.name, self.__witness1.dialogue)
                            # Nested loop to handle mini-game invitation from witness
                            while True:
                                try:
                                    minigame_input = int(input("\nDo you want to play this game?"
                                                               "\n 1 = yes"
                                                               "\n 2 = no \n"))
                                    self.__logger.log("Interacted with the Witness.")
                                    if minigame_input == 1:
                                        # Starts the minigame if player agrees
                                        self.mini_game()
                                        break
                                    elif minigame_input == 2:
                                        # Ends the interaction if player declines
                                        print("ok your loss")
                                        break
                                    else:
                                        # Handles invalid mini game input
                                        raise ValueError(f"{minigame_input}")
                                except ValueError as e:
                                    print(f"Please choose between 1 and 2")
                                    # Error handling for incorrect minigame input
                                    self.__error_logger.log(f"Wrong value entered: {e}")
                                except Exception as ve:
                                    # General error handling during mini game
                                    print(f"Unexpected error occurred.")
                                    self.__error_logger.log(f"Unexpected Error: {ve}")
                        else:
                            # Witness no longer wants to interact
                            print("Witness doesn't want to talk anymore")

                    elif character == 2:
                        # Interacting with the butler in the lobby
                        print(self.__npc1.name, self.__npc1.dialogue)
                        self.__logger.log("Interacted with the Butler")
                        break
                    elif character == 3:
                        # Exiting interaction menu
                        break
                    else:
                        raise ValueError(f"{character}")
                except ValueError as e:
                    # Error handling for incorrect input
                    print(f"Please choose between 1, 2, or 3")
                    self.__error_logger.log(f"Wrong value entered: {e}")
                except Exception as ve:
                    # Error handling for general errors
                    print(f"Unexpected error occurred.")
                    self.__error_logger.log(f"Unexpected Error: {ve}")

        # Handling interactions in upstairs hallway
        elif self.current_room == "upstairs hallway":
            if not self.__trigger_ghost1:
                print("\nyou speak to the Ghost: ")
                print(self.__npc_ghost1.name, self.__npc_ghost1.dialogue)
                self.__trigger_ghost1 = True
                self.__logger.log("Spoke to the ghost in the upstairs hallway")
            else:
                print("\nThere is nobody here to interact with")

        elif self.current_room == "door2":
            while True:
                try:
                    # Error handling block
                    character = int(input("\nIf you want to speak to a witness  "
                                          "choose 1: \nIf you'd like to speak to a mo "
                                          "choose 2: "
                                          "\nIf you'd like to exit from this menu"
                                          "choose 3: "))

                    if character == 1:
                        if not self.__interact_witness2:
                            print(self.__witness2.name, self.__witness2.dialogue)
                            self.__crime_scene.add_clue("Safe code must be a combination of the numbers 3,6,7")
                            self.__interact_witness2 = True
                            self.__logger.log("Interacted with the Witness in door 2")
                            break
                        else:
                            print("The witness is too busy cleaning.")
                            break

                    elif character == 2:
                        print(self.__npc2.name, self.__npc2.dialogue)
                        self.__logger.log("Interacted with Mo")
                        break
                    elif character == 3:
                        break
                    else:
                        raise ValueError(f"{character}")
                except ValueError as e:
                    # Error handling for incorrect values
                    print(f"Please choose between 1, 2, or 3")
                    self.__error_logger.log(f"Wrong value entered: {e}")
                except Exception as ve:
                    # Error handling for general errors
                    print(f"Unexpected error occurred.")
                    self.__error_logger.log(f"Unexpected Error: {ve}")

        # Handling interactions in meeting room
        elif self.current_room == "meeting room":
            if self.__interact_suspect1 and self.__interact_suspect2:
                print("you speak to the Mrs. Hooch, the owner of the mansion and the missing necklace: ")
                print(self.__npc3.name, self.__npc3.dialogue)
                while True:
                    # Error handling block
                    try:
                        meeting_choice = int(input("Do you want to call a meeting and out the thief?"
                                                   "\nPress 1 to call a meeting "
                                                   "\nPress 2 to take more time and leave the room: "))
                        if meeting_choice == 1:
                            print("Everybody is present in the room, gathered around a round table to "
                                  "hear your decision."
                                  "\n'So who was it' Mrs Hooch exclaims ")
                            # Nested error handling
                            try:
                                thief_choice = (int(input("Enter the name of the thief!"
                                                          "\n1 = Sam Everton"
                                                          "\n2 = Samantha Evans"
                                                          "\n3 = Josh Burn")))
                                # Thief choices
                                if thief_choice == 1:
                                    print("\nIn the tense meeting room, you exposed Sam Everton as the thief."
                                          "\nGasps echoed as the stolen necklace was revealed."
                                          "\nWith a firm look, you signaled the police. "
                                          "\nOfficers swiftly moved in, handcuffing Sam amidst the shocked onlookers. "
                                          "\nThe stolen necklace glinted on the table, soon to be returned. "
                                          "\nJustice served, the room cleared, leaving behind "
                                          "the quiet satisfaction of a "
                                          "closed case.")
                                    self.__running = False

                                elif thief_choice == 2:
                                    print("In the charged meeting room, you point at Samantha Evans,"
                                          "convinced she was the thief.\nGasps filled the air as "
                                          "the room buzzed with disbelief."
                                          "\nOfficers hesitate, but reluctantly move in to detain Samantha."
                                          "\nAs she protested her innocence, the stolen necklace remained a mystery. "
                                          "\nThe real thief, still at large, left the room unnoticed. The atmosphere "
                                          "shifted,"
                                          "\nheavy with the weight of a mistake. Samantha, wrongly accused, was led "
                                          "away,"
                                          "\nand the true culprit vanished into the shadows."
                                          "\nThe stolen necklace, now lost in the confusion,"
                                          "\nmarked the bitter end of a case gone awry.")
                                    self.__running = False

                                elif thief_choice == 3:
                                    print("In the charged meeting room, you point at Josh Burn,"
                                          "convinced he was the thief."
                                          "\nGasps filled the air as the room buzzed with disbelief."
                                          "\nOfficers hesitate, but reluctantly move in to detain Josh."
                                          "\nAs he protested his innocence, the stolen necklace remained a mystery. "
                                          "\nThe real thief, still at large, left the room unnoticed. "
                                          "The atmosphere shifted,"
                                          "\nheavy with the weight of a mistake. Josh, wrongly accused, was led away,"
                                          "\nand the true culprit vanished into the shadows."
                                          "\nThe stolen necklace, now lost in the confusion,"
                                          "\nmarked the bitter end of a case gone awry.")
                                    self.__running = False
                                else:
                                    raise ValueError(f"{thief_choice}")
                            except ValueError as e:
                                # Handle error for incorrect input
                                print(f"Please choose between 1, 2, or 3")
                                self.__error_logger.log(f"Wrong value entered: {e}")
                            except Exception as ve:
                                # General error handling
                                print(f"Unexpected error occurred.")
                                self.__error_logger.log(f"Unexpected Error: {ve}")

                        elif meeting_choice == 2:
                            self.current_room = "upstairs hallway"
                            break
                        else:
                            raise ValueError(f"{meeting_choice}")
                    except ValueError as e:
                        # Error handling for incorrect input
                        print(f"Please choose between 1 and 2")
                        self.__error_logger.log(f"Wrong value entered: {e}")
                    except Exception as ve:
                        # General error handling
                        print(f"Unexpected error occurred.")
                        self.__error_logger.log(f"Unexpected Error: {ve}")
            else:
                print("nobody is in the meeting room."
                      "\nTIP: You must interact with all the suspects to call a meeting")
        # End if
        elif self.current_room == "downstairs hallway":
            if self.__trigger_ghost1:
                print("\nyou speak to the Ghost: ")
                print(self.__npc_ghost2.name, self.__npc_ghost2.dialogue)
                self.__trigger_ghost1 = False
                self.__logger.log("Spoke to the ghost in the downstairs hallway")
            else:
                print("\nThere is nobody here to interact with")

        elif self.current_room == "storage room":
            if not self.__interact_suspect3:
                print("\nYou are interacting with Josh Burn")
                print(self.__suspect3.name, self.__suspect3.dialogue)
                self.__logger.log("Interacted with Josh Burn")
                if self.__IDcard:
                    while True:
                        # Error handling block
                        try:
                            player_input = int(input("\n Give him his ID card?"
                                                     "\n1 = yes"
                                                     "\n2 = no"))
                            if player_input == 1:
                                print(
                                    "Thank You soo much, I always forget things "
                                    "\nbut I'm pretty sure that biology nerd took my ID card "
                                    "As a reward I'll give you the key for the kitchen,"
                                    "\n you should probably check there before the meeting")
                                self.__kitchen_key = True
                                self.__interact_suspect3 = True
                                self.__logger.log("Gave Josh Burn his ID card")
                                break
                            elif player_input == 2:
                                print("Well if you see my ID card please give it to me")
                                self.__logger.log("didn't give Josh Burn his ID card")
                            else:
                                raise ValueError(f"{player_input}")
                        except ValueError as e:
                            # Error handling for incorrect input
                            print(f"Please choose between 1 and 2")
                            self.__error_logger.log(f"Wrong value entered: {e}")
                        except Exception as ve:
                            # Error handling for general errors
                            print(f"Unexpected error occurred.")
                            self.__error_logger.log(f"Unexpected Error: {ve}")

                else:
                    print("You dont have the ID card\nTIP: you should go upstairs and look for it")
            else:
                print("Seems like Josh Burn left the room.")

        elif self.current_room == "Kitchen":
            while True:
                # Error handling block
                try:
                    character = int(input("If you want to speak to Sam Everton "
                                          "choose 1. \nIf you'd like to speak to Samantha Evans "
                                          "choose 2: "
                                          "\nIf you'd like to exit this menu"
                                          "choose 3: "))

                    if character == 1:
                        if not self.__interact_suspect1:
                            print(self.__suspect1.name, self.__suspect1.dialogue)
                            self.__interact_suspect1 = True
                            self.__logger.log("interacting with sam")
                        while True:
                            try:
                                confront_choice = int(input("\n 'Missing page from a biology book?'"
                                                            "\nThat is quite familiar you think to yourself"
                                                            "\nwould you like to confront Sam? You might be "
                                                            "better off keeping"
                                                            "your cards close to your chest"
                                                            "\n1=yes"
                                                            "\n2=no\n"))

                                if confront_choice == 1:
                                    if self.__knife:
                                        print("\nIn a sudden and alarming turn of events,"
                                              "\nSam Panics charged toward you with a knife in hand."
                                              "\nReacting on instinct, you swiftly drew your own knife, "
                                              "\nmeeting the imminent threat head-on. "
                                              "\nThe clash of metal echoed in the air as the blades collided. "
                                              "\nIn a dance of survival, you skillfully defended yourself, "
                                              "\nensuring that the dangerous encounter was swiftly brought"
                                              " under control. "
                                              "\nThe tension lingered, but with your own blade in hand, "
                                              "you stood unscathed, "
                                              "\nhaving successfully thwarted the unexpected assault.")
                                        self.__running = False

                                    else:
                                        print("\nIn a sudden and alarming turn of events,"
                                              "\nSam panics and charges toward you with a knife in hand."
                                              "\nCaught off guard and defenseless, you attempted to evade the attack,"
                                              "\nbut the swift assault overwhelmed you."
                                              "\nThe glint of the blade was the last thing you saw as the encounter "
                                              "took a tragic turn,"
                                              "\nand Sam's aggression proved fatal. The room fell silent,"
                                              "\nthe clash of metal replaced by an eerie stillness,"
                                              "\nmarking the abrupt and unfortunate end to the encounter.")
                                        self.__running = False
                                    break

                                elif confront_choice == 2:
                                    print("\nYou decide to not rush into a decision, smart thinking!")
                                    break
                                else:
                                    raise ValueError(f"{confront_choice}")
                            except ValueError as e:
                                # Error handling for incorrect input
                                print(f"Please choose between 1 and 2")
                                self.__error_logger.log(f"Wrong value entered: {e}")

                            except Exception as ve:
                                # Error handling for general errors
                                print(f"Unexpected error occurred.")
                                self.__error_logger.log(f"Unexpected Error: {ve}")
                        # Break loop
                        break
                    elif character == 2:
                        if not self.__interact_suspect2:
                            print(self.__suspect2.name, self.__suspect2.dialogue)
                            self.__interact_suspect2 = True
                            break
                        else:
                            print("OMG what else do you want, like piss off!")
                        break
                    elif character == 3:
                        break
                    else:
                        raise ValueError(f"{character}")
                except ValueError as e:
                    # Error handling for incorrect input
                    print(f"Please choose between 1, 2, or 3")
                    self.__error_logger.log(f"Wrong value entered: {e}")
                except Exception as ve:
                    # Error handling for general errors
                    print(f"Unexpected error occurred.")
                    self.__error_logger.log(f"Unexpected Error: {ve}")

    def examine_room(self):

        if self.current_room == "lobby":
            print("\nyou are in the lobby: "
                  "The mansion lobby is a blend of timeless elegance with marbled floors,"
                  "a dazzling chandelier, \nand antique furniture. ")
            self.__logger.log("examine the lobby")

        elif self.current_room == "upstairs hallway":
            print("\nyou are in the upstairs hallway "
                  "The hallway is adorned with elegant carpets,"
                  " bright fixtures, \nand family portraits that share the history of its residents.")
            self.__logger.log("examine the upstairs hallway")
        elif self.current_room == "door2":
            print("\nYou entered door 2... It is a small, bear room with a bed and a safe,")
            if not self.__safe_opened:
                while True:
                    # Error handling block
                    try:
                        safe_choice = int(input("\nWould you like to try crack the safe?"
                                                "\nTheir could be vital evidence inside!"
                                                "\n1=yes"
                                                "\n2=no"))
                        if safe_choice == 1:
                            safe_code = int(input("\nEnter the 3 digit code to open the safe..."))

                            if safe_code == 763:
                                print("You enter the code and pull the handle, the safe door creeks open "
                                      "slowly to reveal;"
                                      "\nan ID card belonging to Josh Burn"
                                      "\na page of a biology book, seems to be on the DNA chapter"
                                      "\na diamond from the necklace, was wrapped by that biology page"
                                      "\na handkerchief with the initials S.E."
                                      "\ntorn piece of leopard fur")  # add stuff for safe
                                self.__IDcard = True
                                self.__crime_scene.add_inventory("ID CARD")
                                self.__crime_scene.add_clue("page from a biology book")
                                self.__crime_scene.add_clue("a diamond from the missing necklace")
                                self.__crime_scene.add_clue("handkerchief with the initials S.E.")
                                self.__crime_scene.add_clue("torn piece of leopard fur")
                                self.__safe_opened = True
                                break

                            else:
                                print("\nYou enter the code and pull the handel... it wont budge!")
                                break

                        elif safe_choice == 2:
                            print("\nYou decided to not crack the safe")
                            break

                        else:
                            raise ValueError(f"{safe_choice}")

                    except ValueError as e:
                        # Error handling for incorrect input
                        print(f"Please choose between 1 and 2")
                        self.__error_logger.log(f"Wrong value entered: {e}")

                    except Exception as ve:
                        # Error handling for general error
                        print(f"Unexpected error occurred.")
                        self.__error_logger.log(f"Unexpected Error: {ve}")
            else:
                print("\nYou already opened the safe\n")

        elif self.current_room == "meeting room":
            print("\nYou are in the meeting room"
                  "The meeting room is professional and well-lit,"
                  " featuring a polished table, comfortable chairs,\n"
                  " and a sleek screen for presentations."
                  " It's designed for focused discussions and collaborative decision-making.")
            if self.__interact_suspect1 and self.__interact_suspect2:
                print("\n\nMs. hootch is sitting there looking at you, looks like she wants to talk to you, "
                      "\nyou should interact with others in the room")
            self.__logger.log("examine the meeting room")

        elif self.current_room == "downstairs hallway":
            print("\nYou are in the downstairs hallway"
                  "The lower-level hallway is a cozy passage,\n"
                  " softly lit, with warm-toned wooden floors, creating a homey and familiar ambiance.")
            self.__logger.log("examine the downstairs hallway")

        elif self.current_room == "storage room":
            print("\nYou are in the storage room "
                  "\nThe storage room is organized, "
                  "\nwith neatly labeled boxes and shelves holding tools and supplies.")
            self.__logger.log("examine the storage room")

            if not self.__knife:
                while True:
                    # Error handling block
                    try:
                        # User input
                        knife_choice = int(input("\nYou notice a knife on top of one of the boxes, "
                                                 "\nThis could be useful in the future, "
                                                 "\nWould you like to pick it up?"
                                                 "\n1=yes"
                                                 "\n2=no: \n"))

                        if knife_choice == 1:
                            self.__knife = True
                            self.__crime_scene.add_inventory("knife")
                            print("\nYou added the knife to your inventory")
                            self.__logger.log("Added the knife to your inventory")
                            break

                        elif knife_choice == 2:
                            print("\nYou decided to not pick up the knife")
                            self.__logger.log("Decided to not pick up the knife")
                            break

                        else:
                            raise ValueError(f"{knife_choice}")

                    except ValueError as e:
                        # Error handling for incorrect input
                        print(f"Please choose between 1 and 2")
                        self.__error_logger.log(f"Wrong value entered: {e}")

                    except Exception as ve:
                        # Error handling for general errors
                        print(f"Unexpected error occurred.")
                        self.__error_logger.log(f"Unexpected Error: {ve}")
            else:
                pass

        elif self.current_room == "Kitchen":
            print("\nYou are in the kitchen"
                  "The kitchen buzzes with stainless steel appliances "
                  "and a welcoming aroma.\n "
                  "Well-organized counter tops and a cozy dining area contribute to its charm.")
            self.__logger.log("examine the kitchen")

    def choose_door(self):
        # ...
        self.__logger.log("Doors are to be chosen: ")
        # ...

        print("\nYou decide to choose a door to investigate:")
        # nice output to show which door leads to what.

        if self.current_room == "lobby":
            while True:
                # Error handling block
                try:
                    door_choice = int(input("\nchoose 1 to go to the upstairs hallway: "
                                            "\nchoose 2 to go to the downstairs hallway: "
                                            "\nchoose 3 to exit from this menu: "))
                    if door_choice == 1:
                        print("\nYour now in the upstairs hallway")
                        self.current_room = "upstairs hallway"
                        self.__logger.log("Upstairs hallway door was chosen")
                        break

                    elif door_choice == 2:
                        print("\nYour now in the downstairs hallway")
                        self.current_room = "downstairs hallway"
                        self.__logger.log("Downstairs hallway door chosen")
                        break

                    elif door_choice == 3:
                        break

                    else:
                        raise ValueError(f"{door_choice}")

                except ValueError as e:
                    # Error handling message for incorrect value
                    print(f"Please choose between 1, 2, or 3")
                    self.__error_logger.log(f"Wrong value entered: {e}")

                except Exception as ve:
                    # Error handling for general errors
                    print(f"Unexpected error occurred.")
                    self.__error_logger.log(f"Unexpected Error: {ve}")

        elif self.current_room == "upstairs hallway":
            while True:
                # Error handling block
                try:
                    door_choice = int(input("\nchoose 1 to go the 3 mystery doors (BE CAREFUL!): "
                                            "\nchoose 2 to go to the meeting room: "
                                            "\nchoose 3 to go back to the lobby: "
                                            "\nchoose 4 to stay in the upstairs hallway: "))

                    if door_choice == 1:
                        if self.__trigger_ghost1:
                            while True:
                                try:
                                    door_choice = int(input("\nchoose 1 to enter door 1: "
                                                            "\nchoose 2 to enter door 2: "
                                                            "\nchoose 3 to enter door 3: "
                                                            "\nchoose 4 to stay in the upstairs hallway: "))
                                    self.__logger.log("Mystery door chosen in upstairs hallway")
                                    if door_choice == 1:
                                        print("\nYou go into the room and suddenly the floor cracks and "
                                              "before you know it you fall through the floor and die.")
                                        self.__running = False
                                        self.__logger.log("Chose door 1 from mystery door choice")
                                        break

                                    elif door_choice == 2:
                                        print("\nYour now in room 2")
                                        self.current_room = "door2"
                                        self.__trigger_ghost2 = True
                                        self.__logger.log("Chose door 2 from Mystery door choice")
                                        break

                                    elif door_choice == 3:
                                        print(
                                            "\nYou enter a creepy but empty room, there an open window you decide "
                                            "to look at,look out the window and down and you see an open trash bin, "
                                            "\nsuddenly you hear the floor cracking from a foot step and before "
                                            "you could turn "
                                            "around you get murdered and thrown out the window and into the bin."
                                            "\nYOU DIED")
                                        self.__running = False
                                        self.__logger.log("Chose door 3 from Mystery door choice")
                                        break

                                    elif door_choice == 4:
                                        print("\nYou are back to the upstairs hallway")
                                        self.current_room = "upstairs hallway"
                                        self.__logger.log("Chose door 4 from Mystery door choice")
                                        break
                                    else:
                                        # Error message for invalid choice
                                        raise ValueError(f"{door_choice}")
                                except ValueError as e:
                                    # Error handling for incorrect value
                                    print(f"Please choose between 1, 2, 3, or 4")
                                    self.__error_logger.log(f"Wrong value entered: {e}")
                                except Exception as ve:
                                    # Error handling for general errors
                                    print(f"Unexpected error occurred.")
                                    self.__error_logger.log(f"Unexpected Error: {ve}")
                        else:
                            print("\nYou must interact with the ghost in the upstairs hallway to "
                                  "gain access to this room")
                        break

                    elif door_choice == 2:
                        print("\nYou entered the meeting room")
                        self.current_room = "meeting room"
                        break

                    elif door_choice == 3:
                        print("\nYour back in the lobby")
                        self.current_room = "lobby"
                        self.__logger.log("Chose to go back to the lobby")
                        break
                    elif door_choice == 4:
                        print("\nYou are back to the upstairs hallway")
                        self.current_room = "upstairs hallway"
                        self.__logger.log("Chose door 4 from Mystery door choice")
                        break
                    else:
                        raise ValueError(f"{door_choice}")
                except ValueError as e:
                    # Error handling for incorrect value
                    print(f"Please choose between 1, 2, 3, or 4")
                    self.__error_logger.log(f"Wrong value entered: {e}")
                except Exception as ve:
                    # Error handling for general errors
                    print(f"Unexpected error occurred.")
                    self.__error_logger.log(f"Unexpected Error: {ve}")

        elif self.current_room == "door2":
            while True:
                try:
                    # Error handling block
                    door_choice = int(input("\nchoose 1 to leave room 2: "
                                            "\nchoose 2 to stay in room 2"))

                    if door_choice == 1:
                        print("\nYou left room 2 and now in the upstairs hallway.")
                        self.current_room = "upstairs hallway"
                        self.__logger.log("Chose to leave room 2 and went back to upstairs hallway")
                        break

                    elif door_choice == 2:
                        print("\nYour still in room 2")
                        self.current_room = "door2"
                        self.__logger.log("Chose to stay in room 2")
                        break
                    else:
                        raise ValueError(f"{door_choice}")
                except ValueError as e:
                    # Error handling for incorrect values
                    print(f"Please choose between 1 and 2")
                    self.__error_logger.log(f"Wrong value entered: {e}")
                except Exception as ve:
                    # Error handling for general errors
                    print(f"Unexpected error occurred.")
                    self.__error_logger.log(f"Unexpected Error: {ve}")

        elif self.current_room == "meeting room":
            while True:
                try:
                    # Error handling for incorrect values
                    door_choice = int(input("\nchoose 1 to go to the upstairs hallway: "
                                            "\nchoose 2 to stay in the meeting room: "))

                    if door_choice == 1:
                        print("\nYou left the meeting room and are now in the upstairs hallway.")
                        self.current_room = "upstairs hallway"
                        self.__logger.log("Chose to go to the upstairs hallway")
                        break

                    elif door_choice == 2:
                        print("\nYour still in the meeting room")
                        self.current_room = "meeting room"
                        self.__logger.log("Chose to stay in the meeting room")
                        break
                    else:
                        raise ValueError(f"{door_choice}")
                except ValueError as e:
                    # Error handling for incorrect values
                    print(f"Please choose between 1 and 2")
                    self.__error_logger.log(f"Wrong value entered: {e}")
                except Exception as ve:
                    # Error handling for general errors
                    print(f"Unexpected error occurred.")
                    self.__error_logger.log(f"Unexpected Error: {ve}")

        elif self.current_room == "downstairs hallway":
            while True:
                try:
                    # Error handling block
                    door_choice = int(input("\nchoose 1 to go to the Kitchen: "
                                            "\nchoose 2 to go to the storage room: "
                                            "\nchoose 3 to go back to the lobby: "
                                            "\nchoose 4 to exit from this menu: "))

                    if door_choice == 1:
                        if self.__kitchen_key:
                            print("\nYour now in the Kitchen")
                            self.current_room = "Kitchen"
                            self.__logger.log("Chose to go to the Kitchen")
                        else:
                            print("Door is locked, find the key to open it")
                        break

                    elif door_choice == 2:
                        if self.__trigger_ghost2:
                            print("\nYour now in the storage room")
                            self.current_room = "storage room"
                            self.__logger.log("Chose to go into the storage room")
                        elif not self.__trigger_ghost1:
                            print("You must interact with the ghost upstairs and enter the right room")
                        else:
                            print("You must interact with the ghost in the downstairs hallway")
                        break

                    elif door_choice == 3:
                        print("\nYour back in the lobby")
                        self.current_room = "lobby"
                        self.__logger.log("Chose to go back to the lobby")
                        break
                    elif door_choice == 4:
                        print("\nYour still in the downstairs hallway")
                        self.current_room = "downstairs hallway"
                        self.__logger.log("Chose to stay in the downstairs hallway")
                        break
                    else:
                        raise ValueError(f"{door_choice}")
                except ValueError as e:
                    # Error handling for incorrect values
                    print(f"Please choose between 1, 2, 3 or 4")
                    self.__error_logger.log(f"Wrong value entered: {e}")
                except Exception as ve:
                    # Error handling for general errors
                    print(f"Unexpected error occurred.")
                    self.__error_logger.log(f"Unexpected Error: {ve}")

        elif self.current_room == "storage room":
            while True:
                try:
                    # Error handling block
                    door_choice = int(input("\nchoose 1 to leave the storage room: "
                                            "\nchoose 2 to stay in storage room"))

                    if door_choice == 1:
                        print("\nYou left the storage room and now in the downstairs hallway.")
                        self.current_room = "downstairs hallway"
                        self.__logger.log("Chose to leave the Storage room")
                        break

                    elif door_choice == 2:
                        print("\nYour still in the storage room")
                        self.current_room = "storage room"
                        self.__logger.log("Chose to stay in the Storage room")
                        break
                    else:
                        raise ValueError(f"{door_choice}")
                except ValueError as e:
                    # Error handling for incorrect values
                    print(f"Please choose between 1 and 2")
                    self.__error_logger.log(f"Wrong value entered: {e}")
                except Exception as ve:
                    # Error handling for general errors
                    print(f"Unexpected error occurred.")
                    self.__error_logger.log(f"Unexpected Error: {ve}")

        elif self.current_room == "Kitchen":
            while True:
                try:
                    # Error handling block
                    door_choice = int(input("\nchoose 1 to leave room 2: "
                                            "\nchoose 2 to stay in room 2"))

                    if door_choice == 1:
                        print("\nYou left the Kitchen and now in the downstairs hallway.")
                        self.current_room = "downstairs hallway"
                        self.__logger.log("Chose to leave room 2")
                        break

                    elif door_choice == 2:
                        print("\nYour still in the Kitchen")
                        self.current_room = "Kitchen"
                        self.__logger.log("Chose to stay in room 2")
                        break
                    else:
                        raise ValueError(f"{door_choice}")
                except ValueError as e:
                    # Error handling for incorrect value
                    print(f"Please choose between 1 and 2")
                    self.__error_logger.log(f"Wrong value entered: {e}")
                except Exception as ve:
                    # Error handling for general errors
                    print(f"Unexpected error occurred.")
                    self.__error_logger.log(f"Unexpected Error: {ve}")

    def mini_game(self):
        while True:
            try:
                # Error handling block

                # User inputs choice to play
                choice = input("Do you want to play? y/n: ")

                # Check if user wants to play
                # If user chooses y game into starts
                if choice.lower() == 'y':
                    print("The game is called higher or lower. It's pretty easy\n"
                          "I will pick a random number between 1 and 10, and you have 3 tries to guess\n"
                          "the target number. If you choose a number\n"
                          "higher than the target number, I will say lower, and if you choose a lower number,\n"
                          "I will say higher.")
                    self.__logger.log("Chose to play the minigame")

                    # Generate random number between 1 and 10
                    target = random.randint(1, 10)
                    game_won = False

                    # Guessing loop
                    for tries in range(3):
                        try:
                            # User inputs guess
                            guess = int(input("Choose a number: "))

                            # Error checking to make sure user guess is between 1 and 10
                            if 1 <= guess <= 10:
                                if guess > target:
                                    print("Lower, Try again!")
                                elif guess < target:
                                    print("Higher, Try again!")
                                elif guess == target:
                                    print("Well done! You won. I will now tell you all\n"
                                          "the information.\n"
                                          "Check you journal to look at the information")
                                    self.__logger.log("Won the minigame")
                                    game_won = True
                                    break
                            else:
                                print("Invalid input! Please enter a number between 1 and 10")
                        except ValueError:
                            print("Invalid input! Please enter a valid number.")
                            continue
                    else:
                        # Message for user when they run out of tries
                        print(f"You've ran out of tries, the target was {target}, "
                              f"Better luck next time!!")
                        self.__logger.log("Lost the minigame")

                    # Gives user choice to restart or quit game if they didn't win
                    if not game_won:
                        play_again = input("Would you like to give it another try?: ")
                        if play_again.lower() == 'n':
                            print("Ok, your loss!")
                            break
                    # Exit the loop if the game is won or over
                    if game_won:
                        self.__crime_scene.add_biography(self.__suspect1_information)
                        self.__crime_scene.add_biography(self.__suspect2_information)
                        self.__crime_scene.add_biography(self.__suspect3_information)
                        self.__interact_witness1 = True
                        break

                # If user inputs no displays message and game ends
                elif choice.lower() == 'n':
                    print("Ok, your loss!")
                    break

                # Raise an error for invalid input
                else:
                    raise ValueError("Invalid input! Please enter 'y' or 'n'.")

            # Displays Value error message as e
            except Exception as e:
                print(f"An error occurred: {e}")
