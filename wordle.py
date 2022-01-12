# Zeke Farkas
# My attempt at making wordle for command line

import csv
import random
from termcolor import colored

MAX_TURNS = 5

def gameLoop(MAX_TURNS):
    # Import list of words
    with open('words.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        words = list(reader)
    

    # Pick random word
    answer = random.choice(words)[0].upper()

    # Initiallize
    win = False
    currTurn = 1
    userGuess = ['','','','','','']
    prevGuess  = ['_ _ _ _ _ ','','','','','']
    wrongLetters = []

    # Game loop
    while currTurn <= MAX_TURNS:
        # Print turn numer and previous wrong letters guessed
        if currTurn == 1:
            print('TURN ' + str(currTurn))
        else:
            print('TURN ' + str(currTurn) + " | Wrong guessed letters: " + ' '.join([str(elem) for elem in wrongLetters]))
        
        # Print previous guess with either red (letter in word but wrong place) or 
        # green (letter in right place) letter, or _ for letter not in word
        print(prevGuess[currTurn-1])
        userGuess[currTurn] = input("Enter your guess: ").upper()
        if len(userGuess[currTurn]) != 5:
            userGuess[currTurn] = input("Please enter a guess that is 5 letters: ")

        # Check guessed word vs answer, and add to prevGuess based on if letter is right (red, green)
        for i in range(5):
            if userGuess[currTurn][i] == answer[i]:
                prevGuess[currTurn] += colored(answer[i], 'green') + ' '
            elif userGuess[currTurn][i] in answer:
                prevGuess[currTurn] += colored(userGuess[currTurn][i], 'red') + ' '
            else:
                prevGuess[currTurn] += '_ '
                wrongLetters.append(userGuess[currTurn][i])

        # Check if guessed word is correct
        if userGuess[currTurn] == answer:
            win = True
            break

        print('--------------')
        currTurn += 1

    # Check for win or loss
    if win:
        print("You win! Congrats! The word was " + answer)
    else:
        print("Sorry, better luck next time. The word was " + answer)

if __name__ == "__main__":
    # Run game
    gameLoop(MAX_TURNS)


    # Ask to play again
    ans = input("Play again? Y | N  : ")
    loop = True

    while loop:
        if ans == 'Y' or ans == 'y' or ans == 'Yes' or ans == 'yes' or ans == 'YES':
            gameLoop(MAX_TURNS)
            ans = ''
        elif ans == 'N' or ans == 'n' or ans == 'No' or ans == 'no' or ans == 'NO':
            loop = False
            ans = ''
            break
        else:
            ans = input("That answer is not recognized, please enter either Y or N: ")
