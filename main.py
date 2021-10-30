# Hunter C. Sylvester
# Purpose: Create a guessing game with values 1-100 inclusive.  The player will have unlimited attempts to
#          guess the correct number. This saves the top 5 player's scores and writes them to a txt file.
#

# Import modules needed to create this program
# This helps with creating a random number
import random
from library import *

# The instructions of the game
print("Welcome to the Number Guessing Game! \n1. You will randomly choose a number between 1 and 100 inclusive. \n2. I will let"
      ' you know if it is high, low, or correct. \n3. You can continue by inputting a number or pressing "q" to quit. \n')

# Have i set to 0 for counting and compGuess for the random number guessed by the computer
i = 0
compGuess = 4#random.randint(1, 100)

topPlayers = []

# Name of player
while True:
    playersName = input("Welcome! What is your name? ")
    if playersName == "":
        print("Please type a name 1 or more characters long.  Thank you!")
    else:
        break

# Create a loop to continue guessing until you get the number correct
while True:
    # Creates a loop to count how many times a player guesses and gives a hint if their value is wrong
    try:
        yourGuess = (input("Please pick a natural number between 1-100 inclusive: "))
        if str(yourGuess) == "q":
            print(f"Thank you so much for playing {playersName}, please come again!!!"
                  f"Here are the top scores as you leave!")
            endersGame()
            exit()

        while yourGuess != compGuess:
            if 100 >= int(yourGuess) >= 1:
                if int(yourGuess) < compGuess:
                    print("Your value is low, pick another number! ")
                    i += 1
                elif int(yourGuess) > compGuess:
                    print("Your value is high, pick another number! ")
                    i += 1
                break
            else:
                print(f"Sorry {playersName}, that was not a correct input! Remember, only positives! Please try Again!")
                break

        # Congratulates the player for guessing the correct guess and gives how many tries it took
        if int(yourGuess) == compGuess:
            i = i + 1
            print(f"Congratulations, {playersName}! You guessed the same value that I did! Woo! Woo!  It only took you", i, "tries!"
                  " Not bad!!! \nThe top scores are: \n")
            # Display top scores with scores function
            scores(playersName, i)
            playAgain = input(str("Would you like to play again? Press [Y] for yes and [N] for no! "))
            if playAgain == "Y":
                i = 0
                compGuess = random.randint(1, 100)
                continue
            elif playAgain == "N":
                print(f"Thank you so much for playing {playersName}, please come again!!!  "
                      f"Here are the top scores as you leave!")
                endersGame()
                break
            else:
                print(f"{playersName} that was not a [Y] or [N].  The game will end! Here are the "
                      f"top scores as you leave! Thanks for playing!!!")
                endersGame()
                break

    except Exception:
        print(f"Sorry {playersName}, that was not a correct input! Please try Again! \n")


