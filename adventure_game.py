import time
import random


def start():

    enemies = ["dragon", "witch", "cyclops", "werewolf", "vampire"]
    enemy = random.choice(enemies)
    swordOfOgoroth = False      

    def getPlayerName():
        while True:
            getPlayerName.playerName = input("what's your name?")
            if getPlayerName.playerName is None:
                print("You didn't input a value, please try again")
                continue            
            else:
                print("welcome", getPlayerName.playerName)
                break

    def toggle(state):
        state = not state

    def gameOver():
        # runs when the game is over
        while True:
            restart = input("Would you like to play again? (y/n)")
            if restart == "y":
                print_pause("Excellent! Restarting the game ...")
                start()
                break
            elif restart == "n":
                print_pause("Thanks for playing! See you next time.")
                quit()
            else:
                print("Invalid input, please try again")
                continue

    def print_pause(text):
        # prints the game lines in 2 seconds intervals
        print(text)
        time.sleep(2)

    def fight():
        # Things that happen when the player fights
        luck = random.randint(0, 1)

        def loseFight():
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the {}".format(enemy))
            print_pause("You have been defeated!")

        def winFight():
            print_pause(
                "You charge head on to the {} with a loud cry .... "
                .format(enemy)
            )
            print_pause(
                "With the sword of Ogoroth, you are able to take down the {}"
                .format(enemy)
            )
            print_pause("you win!")

        def summonSwordOfOgoroth():
            print_pause("------Summoning the sword of Ogoroth------")
            luck = random.randint(0, 1)
            if luck == 1:
                print_pause("Sword successfully summoned.")
                winFight()
            else:
                loseFight()

        if swordOfOgoroth is True:
            winFight()
        elif luck == 1:
            summonSwordOfOgoroth()
        else:
            loseFight()

        gameOver()

    def cave():
        # Things that happen to the player goes in the cave
        luck = random.randint(0, 1)

        if luck == 1:
            print_pause("You peer cautiously into the cave.")
            print_pause("It turns out to be only a very small cave.")
            print_pause("Your eye catches a glint of metal behind a rock.")
            print_pause("You have found the magical Sword of Ogoroth!")
            print_pause(
                "You discard your silly old dagger and take the sword with" +
                " you.")
            print_pause("You walk back out to the field.")
            toggle(swordOfOgoroth)
        else:
            print_pause("You aren't in luck, someone else has summoned the" +
                        " great sword")
            print_pause("You walk back out to the field.")

        action()

    def field():
        # Things that happen when the player runs back to the field
        luck = random.randint(0, 1)

        def escape():
            print_pause(
                "You run back into the field. Luckily, you don't seem to" +
                " have been followed."
            )

        def caught():
            print_pause(
                "Coward! The {} chases you as you run ".format(enemy) +
                "and kills you. You lose!"
            )

        if luck == 1:
            escape()
            action()
        else:
            caught()
            gameOver()

    def house():
        # Things that happen to the player in the house
        print_pause("You approach the door of the house.")
        print_pause(
            "You are about to knock when the door opens and out steps a {}"
            .format(enemy)
        )
        print_pause("EEEE! This is the {}'s house!".format(enemy))
        print_pause("The {} attacks you!".format(enemy))
        if swordOfOgoroth is True:
            print_pause("I feel I am well prepard to fight now")
        else:
            print_pause(
                "You feel a bit under-prepared for this, what with only" +
                " having a tiny dagger."
            )

        while True:
            houseChoice = input("Would you like to (1) fight or (2)" +
                                    " run away?")
            if houseChoice == "1":
                fight()
                break
            elif houseChoice == "2":
                print()
                field()
                break
            else:
                print("Invalid input, please try again")
                continue

    def action():
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause("What would you like to do?")

        while True:
            choice = input("(Please enter 1 or 2)")
            if choice == "1":
                house()
                break
            elif choice == "2":
                cave()
                break
            else:
                print("Invalid input, please try again")
                continue
    
    getPlayerName()

    print_pause(
        "{} finds himself standing in an open field ".format(getPlayerName.playerName) +
        "filled with grass and yellow wildflowers."
    )

    print_pause(
        "Rumor has it that a wicked {} is somewhere ".format(enemy) +
        "around here, and has been terrifying the nearby village."
    )

    print_pause("In front of you is a house.")

    print_pause("To your right is a dark cave.")

    print_pause("In your hand you hold your trusty (but not very effective)" +
                " dagger.")

    print()

    action()


start()
