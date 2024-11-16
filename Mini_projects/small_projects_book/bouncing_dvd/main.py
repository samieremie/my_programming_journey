"""
A program that simulates the bouncing DVD
from back in the days.
"""
import bext, random, sys, time
import numpy as np

WIDTH, HEIGHT = bext.size()

# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

NUMBER_OF_LOGOS = 2  # Changing this will result in multiple logos displayed.
PAUSE_AMOUNT = 0.2 # Try changing this to 1.0 or 0.0.

# Try changing this list to fewer colors:
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

DIRECTIONS = (np.array([2, -1]), np.array([2, 1]), 
              np.array([-2, -1]), np.array([-2, 1]))

# Key names for logo dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def generate_logos():
    """Function that creates a list of logos."""
    logos = []
    for _ in range(NUMBER_OF_LOGOS):
        logos.append({
            COLOR: random.choice(COLORS),
            X: random.randint(1, WIDTH - 4),
            Y: random.randint(1, HEIGHT - 4),
            DIR: random.choice(DIRECTIONS)
            })
    if logos[-1][X] % 2 == 1:
        # Make sure X is even so it can hit the corner and doesn't go out of boundaries.
        logos[-1][X] -= 1
    
    return logos
    
def main():
    """Main function that will display the bouncing logo."""
    bext.clear() # Clear the terminal.
    logos = generate_logos()

    # Count how many times a logo hits a corner.
    corner_bounces = 0 

    while True:                     # Main program loop.
        for logo in logos:          # Handle each logo in the logos list.
            # Erase the logo's current location:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')    # Uncomment this line for no trailing DVD.
            
            # Keep track of how many changes were made.
            changes = 0

            # If the logo bounces off the left or right edge
            if logo[X] <= 0 or logo[X] >= WIDTH - 3:
                # Change the x direction
                logo[DIR][0] *= -1
                # Change color when the logo bounces:
                logo[COLOR] = random.choice(COLORS)
                changes += 1

            # If the logo bounces off the top or bottom edge
            if logo[Y] <= 0 or logo[Y] >= HEIGHT - 1:
                # Change the y direction
                logo[DIR][1] *= -1
                # Change color when the logo bounces:
                logo[COLOR] = random.choice(COLORS)
                changes += 1

            if changes == 2:
                corner_bounces += 1

            # Move the logo
            logo[X] += logo[DIR][0]
            logo[Y] += logo[DIR][1]

            # Clamp X and Y to ensure they remain within bounds:
            logo[X] = max(0, min(WIDTH - 3, logo[X]))
            logo[Y] = max(0, min(HEIGHT - 1, logo[Y]))

        # Display number of corner bounces:
        bext.goto(5, 0)
        bext.fg('black')
        print(f'Corner bounces: {corner_bounces}', end='')

        for logo in logos:
            # Draw the logos at their new location:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)
        sys.stdout.flush() # (Required for bext-using programs.)
        time.sleep(PAUSE_AMOUNT)

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        bext.clear()
        print()
        print('Bouncing DVD Logo, by Samuel Ieremie')
        sys.exit() # When Ctrl-C is pressed, end the program.