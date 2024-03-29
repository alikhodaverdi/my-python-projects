import random


NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(
        """
    Bagels , a deductive logic game designed by Mehrdad
    
    
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is.Here are some clues:
    
    When I say:    That means:
    Mehrdad           One digit is correct but in the wrong position.
    Ali               One digit is correct and in the right position.
    Bagels            No digit is correct. 
    
    And yes i use my names.
    
    For example,if the secret number was 248 and your guess was 843 , the clues would be mehrdad ali   
    """.format(
            NUM_DIGITS
        )
    )
    while True:  # Min game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print("I have thought up a number")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # keep looping until theu enter a valid guess :
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}:".format(numGuesses))
                guess = input(">")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # Tehre correct
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses")
                print("The answer was{}".format(secretNum))
        # Ask player for play again
        print("Do you want to play again ? yes or no")
        if not input(">").lower().startswith("y"):
            break
    print("Tanks for playing")


def getSecretNum():
    """
    Returns a string made up of NUM_DIGITS unique random digits.
    """

    numbers = list("0123456789")
    random.shuffle(numbers)  # shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """
    Returns a string with the ali,mehrdad,bagels clues for a guess and secret number pair
    """
    if guess == secretNum:
        return "You got it"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit is in the correct place
            clues.append("Mehrdad")
        elif guess[i] in secretNum:
            # a correct digit is in the Incorrect place
            clues.append("ALI")

    if len(clues) == 0:
        return "Bagels"
    else:
        # Sort the clues into alphabetical order so their original order
        # doesnt  give information away
        clues.sort()
        # make a single string from the list of string clues.
        return "".join(clues)


if __name__ == "__main__":
    main()
