"""
IPO Chart:

  Input: The user will play a game and guess a number from 1-100 (anything else will not be accepted).


  Output: The program will return whether the user guessed too high or too low. If the user guesses correctly,
  they win and the program ends.
"""

import random
from random import randint

# This will return a random number

def getGuess(minValue, maxValue):
    return random.randint(minValue, maxValue)

def guessWin(guessNum, randomNum):

    randomNum = getGuess(1, 100)
    guessNum = ""

# This function will prompt the user with 7 tries to guess a number from 1-100

    NUMBER_OF_ROUNDS = 0

    for count in range(1, 8):
        NUMBER_OF_ROUNDS += 1
        print("Round ", NUMBER_OF_ROUNDS, " of 7")
        print("-----------------------------")
        while True:
            guessNum = input("Enter your guess (1-100): ")

            if guessNum.isdigit():
                guessNum = int(guessNum)

    # This will print if the user inputs anything outside the range 1-100

                while guessNum <= 0 or guessNum > 100:
                    print("Error ... Incorrect Number. Try Again")
                    break
                else:

    # This will return whether the user guessed too high or too low

                    if guessNum > randomNum:
                        print(" ---> ", guessNum, "is too High ... \n")
                        break
                    elif guessNum < randomNum:
                        print(" ---> ", guessNum, "is too Low ... \n")
                        break

    # This will congratulate the user if they guess correctly

                    else:
                        print("Congratulations ... You guessed the Mystery Number!")
                        return
    # This will print if user inputs anything other than an integer

            else:
                print("Error ... Incorrect Number. Try Again")



# The main function will generate the main prompt of the guessing game

def main():

    tryAgain = ""
    num = ""
    guess = ""

    print("Guess the Mystery Number ... \n")
    guessWin(num, guess)

# This prompt appears after the user has guessed correctly or has used up all rounds

    while tryAgain != "n" or tryAgain != "y":
        tryAgain = input("Would you like to try again (y/n)?: ")
        if tryAgain == "y":
            return main()
        elif tryAgain == "n":
            quit()
        else:
            print("Error ... Invalid Input")



if __name__ == "__main__":
    main()








