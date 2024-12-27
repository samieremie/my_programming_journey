 # If the number doesn't match check for each digit if it matches.
import random as r

def get_clues(user_number, guess_number, number_of_digits):
    """
    Checks for each digit if the number given matches
    the number to guess.

    Returns the clues message to print.
    """
    clues = []
    for i in range(0, number_of_digits):
        # If the digit is in the number and at the correct place.
        if user_number[i] == guess_number[i]:
            clues.append("Fermi")
        # If the digit is in the number but at the wrong place.
        elif user_number[i] in guess_number:
            clues.append("Pico")
    
    # There is no clue to print
    if len(clues) == 0:
        return "Bagels"
    
    # Change the order of the clues
    clues.sort()

    text = ""
    for clue in clues:
        text += clue + " "
    return text

def secret_number(number_digits):
    """Make a n digit random number to guess"""
    number_to_guess = ""
    for _ in range(0, number_digits):
        number_to_guess += str(r.randint(0,9))
    
    return number_to_guess