#!/bin/python3

import random

NUM_DIGITS = 3 
MAX_GUESSES = 10

def main():
    print(''' Bagels, a deductive logic game.
          
I am thinking of a {}-digit number with no repeated digits. 
Try to guess what it is. Here are some clues:
When I say:       That means:
    Pico          One digit is correct but in the wrong position.
    Fermi         One digit is correct and in the right position.
    Bagels        No digits are correct

For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(NUM_DIGITS))
    while True:
        secretNum = generate_secret_number()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGUESSES = 1
        while numGUESSES <= MAX_GUESSES:
            guess = ''
            #Keep looping until user inputs a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGUESSES))
                guess = input('> ')
    
            clues = getClues(guess, secretNum)
            print(clues)
            numGUESSES += 1

            if guess == secretNum:
                break #if guess is correct we break this loop
            if numGUESSES > MAX_GUESSES:
                print('you ran out of guesses')
                print('The answer was {}.'.format(secretNum))
        
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def generate_secret_number() -> str:
    #Generates a random 3-digit number formatted as a string
    secret_number = random.randint(100, 999)
    secretNum = str(secret_number)
    return secretNum
    
def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #correct digit is in the same place
            clues.append(' Fermi ')
        elif guess[i] in secretNum:
            clues.append(' Pico ')
    if len(clues) == 0:
        return 'Bagels' # no correct digits at all
    else:
        #Sort the clues into alphabetical order so their original order
        #doesn't give information away.
        clues.sort()
        #make a single string from the string of list clues.
        return ''.join(clues)
    
    #if the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()