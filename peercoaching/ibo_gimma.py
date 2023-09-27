import time
import os

def clear_terminal():
    os.system("cls")
playing = True
while playing:
    naam = input("Voer je naam in: ")

    print(f"""Welcome to the Adventure Game, {naam}!
    You are on Earth, and you are a traveler who wants to explore different planets.
    You decide to explore three different planets: Mercury, Saturn, Jupiter.
    \nChoose your planet: """)
    time.sleep(2)

    planetChoice_twee = True
    while planetChoice_twee:
        planetChoice = input("> ")

        if planetChoice.lower().capitalize() == "Mercury":
            clear_terminal()
            print("Welcome to Mercury!\n")
            time.sleep(2)
            print("You have landed on the scorching surface of Mercury, the closest planet to the Sun.\n")
            time.sleep(2)
            print("Before you can explore the secrets of the planet, you need to acquire a magic necklace that can withstand the heat of the sun.\n")
            time.sleep(2)
            print("The name of this necklace is... Necklace of Heat.")
            time.sleep(2)
            print("Here's the puzzle:")
            time.sleep(2)
            print("You see the numbers:")
            print("1")
            print("2")
            print("3")
            print("4")
            time.sleep(2)
            print("Choose the right order of numbers.")
            time.sleep(2)
            print("What's your guess? Enter the numbers separated by spaces")

            correct_order = ["2", "3", "4", "1"]

            user_input = input("> ").split()

            if user_input == correct_order:
                print("Congratulations! You've solved the puzzle and unlocked the Necklace of Heat.")
                time.sleep(2)
                print("You can now withstand the heat of the sun with this necklace.")
                time.sleep(2)
                print("You can use this information to continue your exploration.")
            else:
                print("Oops! That's not the correct order.")
                time.sleep(2)
                print("The artifact emits a faint glow and resets the puzzle.")
                time.sleep(2)
                print("Try again!")
                quit()

            planetChoice_twee = False
            exploreChoice_check = True
            while exploreChoice_check:
                
                print("Choose the place you want to explore. You can choose the great valleys of Mercury:\n")
                print("or you can go back to earth")
                print("Your input needs to be 'valleys' or 'earth'")
                exploreChoice = input("> ")

                if exploreChoice == "valleys":
                    print("As you delve deeper into the mysteries of Mercury\n")
                    time.sleep(2)
                    print("You stumble into winding valleys known as the great valleys of Mercury\n")
                    time.sleep(2)
                    print("Explore the hidden mysteries of this valley\n")
                    time.sleep(2)
                    exploreChoice_check = False
                    valley_check = True

                    mercury_quest_labyrinth_check = True
                    while mercury_quest_labyrinth_check:
                        print("Do you want to accept the Mercury labyrinth quest? (yes/no)")
                        mercuryQuest = input("> ")
                        if mercuryQuest == "yes":
                            print(f"Thank you, {naam}, for accepting the quest.\n")
                            time.sleep(2)
                            print("You need to search for the hidden alien artifact.\n")
                            time.sleep(2)
                            print("After you have retrieved the alien artifact, you can read about all the hidden mysteries of the unknown creatures of the planet Mercury\n")
                            time.sleep(2)
                            print(f"You got this, {naam}!\n")
                            time.sleep(2)
                            mercury_quest_labyrinth_check = False
                        elif mercuryQuest == "no":
                            print("Your adventure ends here. Farewell...\n")
                            time.sleep(2)
                            quit()
                        else:
                            print("Invalid input. You can only choose yes or no.")

                elif exploreChoice == "earth":
                    print("after you aquired the necklace of heat\n")
                    print("you chose to return to earth")
                    time.sleep(2)
                    print("*spaceship flies back to earth*\n")
                    time.sleep(2)
                    print("welcome to earth\n")
                    time.sleep(2)
                    print(f"your adventure ends here{naam}\n")
                    time.sleep(2)
                    print("thank you for playing!")
                    quit()
                else:
                    print("invalid input. you can only choose valley or earth")
                    exploreChoice_check = True
                    
                

            mercury_magnetic_quest_check = True
            while mercury_magnetic_quest_check:
                print("Do you want to accept the Mercury labyrinth quest? (yes/no)")
                mercuryMagneticQuest = input("> ")
                if mercuryMagneticQuest == "yes":
                    print(f"Thank you, {naam}, for accepting the quest.\n")
                    time.sleep(2)
                    print("Your quest is to retrieve a Dna monster on Mercury to cure all earth diseases\n")
                    time.sleep(2)
                    print(f"You got this, {naam}!\n")
                    time.sleep(2)
                    mercury_magnetic_quest_check = False
                elif mercuryMagneticQuest == "no":
                    print("Your adventure ends here. Farewell...\n")
                    time.sleep(2)
                    quit()
                else:
                    print("Invalid input. You can only choose yes or no.")

            else:
                print("Invalid input. You can only choose between the magnetic anomaly or the Mercury labyrinth")

            print("You step outside your spaceship and walk, and all of a sudden you find yourself between a laboratory, a cave, and a labyrinth1 on Mercury\n")
            time.sleep(2)
            print("You can choose to go north, east, south, or west")

            navigation_mercury_Check = True
            while navigation_mercury_Check:
                print("Which way do you choose? North, East, South, or West?")
                navigation_mercury = input("> ")
                if navigation_mercury == "east":
                    print("*you enter the laboratory*\n")
                    print("Wow! This laboratory is so big!\n")
                    print("I wonder if I can find the Dna monster here\n")

                    navigation_mercury_Check = False
                elif navigation_mercury == "north":
                    print("*you enter the labyrinth*\n")
                    time.sleep(2)
                    print("What where am I? I am so confused\n")
                    time.sleep(2)
                    print("I think that is a labyrinth\n")
                    time.sleep(2)
                    print("I wonder if I can find anything special in here\n")
                    time.sleep(5)
                    print("*after days of walking and walking, you die of dehydration*")
                    time.sleep(4)

                    print(f"Well played, {naam}! Next time better!")
                    navigation_mercury_Check = True
                    quit()
                    
                    
                elif navigation_mercury == "west":
                    print("*you enter the cave*\n")
                    time.sleep(2)
                    print("Where am I?\n")
                    time.sleep(2)
                    print("Why is it so dark in here?\n")
                    time.sleep(8)
                    print("*you fall, and your head gets crushed by a rock*\n")
                    time.sleep(2)
                    print("Mission failed. You'll get it next time!")
                    navigation_mercury_Check = True
                    quit()
                elif navigation_mercury == "south":
                    print("*you walk back to the spaceship*\n")
                    time.sleep(2)
                    print(f"You return safely to Earth, and your adventure ends! Well done, {naam}!")
                    navigation_mercury_Check = True
                    quit()
                else:
                    print("Invalid input. You can only choose North, East, South, or West.")
                    navigation_mercury_check = True
                    quit()


                print("*you entered the laboratory to search for the Dna monster")
                labratorium_check_2 = True
                while labratorium_check_2:
                    print("""Choose the places you want to go in the laboratory:
                        - the lab
                        - behind the plant
                        - lab center
                        - bathroom
                        - testing room
                        - sample room
                        - cure room""")
                    labratorium_check = input("> ")
                    if labratorium_check == "the lab":
                        print("*you entered the lab*\n")
                        print("You are searching for the Dna monster, but you can't find anything.")
                        labratorium_check_2 = True
                    elif labratorium_check == "behind the plant":
                        print("*you are looking behind the plant*\n")
                        print("You are searching for the Dna monster, but you can't find anything.")
                        labratorium_check_2 = True
                    elif labratorium_check == "lab center":
                        print("*you entered the lab center*\n")
                        time.sleep(2)
                        print("You are searching for the Dna monster, but you can't find anything\n")
                        time.sleep(2)   
                        labratorium_check_2 = True 
                    elif labratorium_check == "bathroom":
                        print("*you entered the bathroom*\n")
                        time.sleep(2)
                        print("You are searching for the Dna monster, but you can't find anything\n")
                        time.sleep(2)       
                        labratorium_check_2 = True 
                    elif labratorium_check == "testing room":
                        print("*you entered the testing room*\n")
                        time.sleep(2)
                        print("You are searching for the Dna monster, but you can't find anything\n")
                        time.sleep(2)        
                        labratorium_check_2 = True
                    elif labratorium_check == "sample room":
                        print("*you entered the sample room*\n")
                        time.sleep(2)
                        print("You are searching for the Dna monster, but all the samples are broken!!\n")
                        time.sleep(2)  
                        labratorium_check_2 = True      
                    elif labratorium_check == "cure room":
                        print("You entered the cure room\n")
                        time.sleep(2)
                        print("You found the Dna monster!!\n")    
                        time.sleep(2)
                        print(f"You can save the Earth, {naam}!\n")
                        time.sleep(2)
                        print("*you fly back to Earth")
                        time.sleep(2)
                        print("Thank you for saving the Earth!\n")
                        time.sleep(2)
                        print(f"Your adventure ends here, {naam}.\n")
                        time.sleep(2)
                        print("Thank you for playing!\n")
                        time.sleep(2)
                        labratorium_check_2 = False
                        quit()

                    else:
                        print("""Invalid input. You can only choose between:
                            - the lab
                            - behind the plant
                            - lab center
                            - bathroom
                            - testing room
                            - sample room
                            - cure room""")
                        labratorium_check_2 = True 