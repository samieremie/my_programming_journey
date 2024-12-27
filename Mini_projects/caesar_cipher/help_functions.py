# The help functions for the caesar cipher programs.

import clipboard as c

# Build a dictionary that will have as keys the characters from a to z
# and as values the position of those characters in the alphabet
alpha_pos = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}

# Build a list that will have all letters. 
# You can get the nth letter by accessing nth index.
alpha_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def translate(message, key, mode):
    """A function that translates a message
    based on a specific key.
    Translating can be encryption or decryption (mode parameter)."""
    global alpha_pos
    global alpha_list

    translated_msg = ""
    for char in message:
        cur_char = char.lower()
        # Check if the char is an alphabet letter.
        if cur_char not in alpha_pos:
            # If not then return the char as the new char.
            new_char = cur_char
        # If it is in the alphabet.
        else:
            position = alpha_pos[cur_char]
            if mode == 'encrypt':
                new_char = alpha_list[(position + key) % 26].upper()
                
            else:
                new_char = alpha_list[(position - key) % 26].lower()

        # Add the new translated character to the final msg.
        translated_msg += new_char

    return translated_msg

def encrypt(message, key, is_main_program=False):
    """Just a high level function that calls translate,
    with mode encrypt."""
    encrypted_msg = translate(message, key, 'encrypt')
    # This portion of code must be run only when the function
    # is imported into the ciphering program.
    if is_main_program:
        c.copy(encrypted_msg)
        print("The encrypted message has been copied to the clipboard.")
    return encrypted_msg

def decrypt(message, key, is_main_program=False):
    """Just a high level function that calls translate,
    with the mode decrypt."""
    decrypted_msg = translate(message, key, 'decrypt')
    # This portion of code must be run only when the function
    # is imported into the ciphering program.
    if is_main_program:
        c.copy(decrypted_msg)
        print("The decrypted message has been copied to the clipboard.")
    return decrypted_msg