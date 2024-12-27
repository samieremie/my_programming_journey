"""This program implements the higher or lower card game."""
import random

SUIT = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'Jack', 'Queen', 'King')

NUMBER_CARDS = 8

def create_deck():
    """Function that creates the initial deck."""
    deck = []
    for suit in SUIT:
        for value, rank in enumerate(RANK):
            current_card = {
                'suit': suit,
                'rank': rank,
                'value': value,
                }
            deck.append(current_card)
    
    return deck


def game(deck):
    """Main program function."""
    points = 0

    while True:
        random.shuffle(deck)

        current_card = deck.pop()
        suit = current_card['suit']
        rank = current_card['rank']
        value = current_card['value']

        print(f"The current card is a {rank} of {suit}.")
        prompt = "Is the next card higher or lower than the current one?\n> "
        answer = input(prompt)
        if answer == 'higher':
            next_card = deck.pop()
            print(f"The next card is a {rank} of {suit}")
            if next_card['value'] > value:
                points += 20
                print("Nice you guessed correctly, you get awarded 20 points.")        
            else:
                points -= 15
                print("You were wrong, try again. 15 points lost.")
            print(f"You current points are {points}")

        elif answer == 'lower':
            next_card = deck.pop()
            print(f"The next card is a {rank} of {suit}")
            if next_card['value'] < value:
                points += 20
                print("Nice you guessed correctly, you get awarded 20 points.")        
            else:
                points -= 15
                print("You were wrong, try again. 15 points lost.")
            print(f"You current points are {points}")
        prompt_2 = "Do you wish to continue or to break the game?\nType 'q' for quitting or any key to continue\n> "
        answer = input(prompt_2)
        if answer == 'q':
            break
        else:
            continue

if __name__ == '__main__':
    deck = create_deck()
    game(deck)