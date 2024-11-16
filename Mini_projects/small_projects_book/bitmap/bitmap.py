"""A program that takes a bitmap as a multiline string
and prints it with whatever character you want."""
import sys
# There are 68 periods along the top and bottom of this string:
# (You can also copy and paste this string from
# https://inventwithpython.com/bitmapworld.txt)
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""
print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

for line in bitmap.splitlines():
    # For each line in the bitmap do:
    for i, bit in enumerate(line):
        # Check if the bit is empty
        if bit == ' ':
            # Change the end parameter to nothing instead of a newline
            print(' ', end='')
        elif bit == '.':
            print('.', end='')
        else:
            print(message[i % len(message)], end='')
    
    print() # Print a newline
