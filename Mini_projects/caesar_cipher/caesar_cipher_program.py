# A small cipher program that uses the caesar cipher.

from help_functions import encrypt, decrypt

# A stack for the keys used for encrypting the messages.
stack_keys = []

def main():
    """The main program."""

    while True:
        prompt_action = "Do you want to start/continue encrypting/decrypting?\n"
        prompt_action += "Press any key to continue, press 'q' to quit."
        action = input(prompt_action)
        if action.lower() == 'q':
            break

        prompt = "Do you want to (e)ncrypt or (d)ecrypt?\n> "
        action = input(prompt)

        if action.lower() == 'e':
            prompt_2 = "Please enter the key to use:\n> "
            key = int(input(prompt_2))

            prompt_3 = "Enter the message you want to encrypt:\n> "
            message = input(prompt_3)

            stack_keys.append(key)
            encrypted_message = encrypt(message, key, is_main_program=True)
            print(encrypted_message)

        elif action.lower() == 'd':
            if stack_keys:
                key = stack_keys.pop()
            else:
                print("Please encrypt a message before decrypting.")
                continue

            prompt_3 = "Enter the message you want to decrypt:\n> "
            message = input(prompt_3)

            decrypted_message = decrypt(message, key, is_main_program=True)

            print(decrypted_message)
        
        else:
            print("Please enter a valid command.")

if __name__ == '__main__':
    main()