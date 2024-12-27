"""
Program that is meant to implement the bagels game.
This game consists in guessing a three-digit-number.
The rules are as follows:
- 10 tries.
- pico: when your guess has a correct digit but at the wrong place
- farmi: when your guess has a correct digit at the correct place
- bagels: no correct digit.
"""

from helper import get_clues, secret_number

# Game constants
NUMBER_DIGITS = 3
MAX_GUESSES = 10

# The program rules
rules = {
    "Pico": "One digit is correct but in the wrong position.",
    "Fermi": "One digit is correct and in the right position.",
    "Bagels": "No digit is correct.",
}

# Text to print at the start of the game
text = "Welcome to Bagel, a deductive logic game.\n\n"
text += f"I am thinking of a {NUMBER_DIGITS}-digit number. Try to guess what it is.\n"
text += "Here are some clues:\n"
text += "When I say:\tThat means:"


# Print the game name and rules first.
print(text)
for key, value in rules.items():
    print(f"{key}\t{value}")
print(f"""I have thought up a number.
Try to guess it in {MAX_GUESSES} tries.
Good Luck!""")


# The program
def bagels_run():
    """The main function that will run the program when called."""
    # Text to print at the start of the game
    text = "Welcome to Bagel, a deductive logic game.\n\n"
    text += f"I am thinking of a {NUMBER_DIGITS}-digit number. Try to guess what it is.\n"
    text += "Here are some clues:\n"
    text += "When I say:\tThat means:"


    # Print the game name and rules first.
    print(text)
    for key, value in rules.items():
        print(f"{key}\t{value}")
    print(f"""I have thought up a number.
Try to guess it in {MAX_GUESSES} tries.
Good Luck!""")
    # Make the number we need to guess.
    number_to_guess = secret_number(NUMBER_DIGITS)

    number_of_guesses = 1
    while number_of_guesses <= MAX_GUESSES:
        user_answer = str(input(f"Guess #{number_of_guesses}:\n> "))
        
        # If the number given is shorter or longer than the number we want.
        if len(user_answer) != NUMBER_DIGITS:
            print("Enter a number that has the requested number of digits.")
            continue
        
        # The end condition
        if user_answer == number_to_guess:
            print("Congratulations you guessed correctly!")
            break
        else:
            # Compute the clues message to print
            clues = get_clues(user_answer, number_to_guess, NUMBER_DIGITS)
            print(clues)
            if number_of_guesses == MAX_GUESSES:
                print(f"You lost. The correct number was {number_to_guess}.")
                break

        # At the end of the loop increment the number of guesses
        number_of_guesses += 1
        
if __name__ == '__main__':
    bagels_run()