# A simple program that brute forces through all the possible combinations.
# It then returns the original message back.
# It autodetects if the message is in english using a library.

from help_functions import decrypt
from langdetect import detect

def main():
    """The main function of the program."""
    prompt = "Enter the Caesar Cipher message to hack.\n> "
    message = input(prompt)

    for key in range(0, 26):
        decrypted_message = decrypt(message, key)
        language = detect(decrypted_message)
        if language == 'en':
            print(f"The original message is:\n{decrypted_message}")
            break

if __name__ == '__main__':
    main()