# Python password generator by @driconrikus
# Ver 0.2
import sys
from random import choices

def generate_password():
    # Here is our pool where we will select the characters to create our password.
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lowercase = [letter.lower() for letter in uppercase]
    symbols = ['!', '@', '#', '$', '%', '&', '*']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    characters = uppercase + lowercase + symbols + numbers

    # This variable will ask how long our password will be, it will print a warning if it's below 8 characters.
    try:
        length = int(input('Please select password length: '))
    except ValueError:
        print("Please enter a number.")
        sys.exit()

    if int(length) < 8:
        print('Warning: Minimum recommended length for a secure password is 8 characters.')

    #This is where the magic happens
    password = choices(characters, k=length)

    return "".join(password)

# This function calls the password generator and prints the password to the user.
def run():
    password = generate_password()
    print('Your new password is: ' + password )

if __name__ == '__main__':
    run()