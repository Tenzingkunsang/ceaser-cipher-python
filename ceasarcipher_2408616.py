def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")
#python

def enter_message():
    """this funtion is to ask user to either eccrypt or decrypt"""
    while True:
        option = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if option in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        message = input("What message would you like to {}? ".format("encrypt" if option == 'e' else 'decrypt')).upper()
        shift_key = input("What is the shift number: ")

        if not shift_key.isdigit():
            print("Invalid Shift input. Please enter a numeric value.")
        elif not 0 <= int(shift_key) <= 25:
            print("Invalid Shift key Please enter a value between 0 and 25.")
        else:
            break

    return option, message, int(shift_key)


def encrypt(message, shift_key):
    """this function is to take the given input from user and encrypt it"""
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr((ord(char) - base + shift_key) % 26 + base)
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(message, shift):
    """function to take the given input and decrypt it"""
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_message += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_message += char
    return decrypted_message


def is_file(filename):
    """this function to check whether the given file name from user is valid or not"""
    try:
        open(filename, 'r')
        return True
    except FileNotFoundError:
        return False


def write_messages(messages):
    """ this function is to create and write result in a new text file"""
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message.upper() + '\n')
    print("Output written to results.txt")


def process_file(filename, mode):
    """ this function  is to process file if user chooses encrypt through file
    """
    messages = []
    while True:
        try:
            shift_key= int(input("What is the shift number: "))
            if 0 <= shift_key <= 25:
                break
            else:
                print("Invalid Shift input . Please enter a value between 0 and 25.")
        except ValueError:
            print("Invalid Shift input. Please enter a numeric value.")

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            messages.append(encrypt(line, shift_key) if mode == 'e' else decrypt(line, shift_key))
    write_messages(messages)


def message_or_file():
    """ this function to ask user to either encrypt or decrypt through console or filename"""
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source in ['f', 'c']:
            break
        else:
            print("Invalid Source")

    if source == 'f':
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")

        return mode, None, filename
    else:
        message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else 'decrypt')).upper()
        return mode, message, None


def main():
    """ In this function all the function used above are used."""
    welcome()
    while True:
        mode, message, filename = message_or_file()

        if filename:
            messages = process_file(filename, mode)
        else:
            while True:
                try:
                    shift = int(input("What is the shift number: "))
                    if 0 <= shift <= 25:
                        break
                    else:
                        print("Invalid Shift. Please enter a value between 0 and 25.")
                except ValueError:
                    print("Invalid Shift input. Please enter a numeric value.")

            messages = [encrypt(message, shift)] if mode == 'e' else [decrypt(message, shift)]
            print('\n'.join(messages).upper())
       

        another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_message != 'y':
            print("Thanks for using the program, goodbye!")
            break

main()
