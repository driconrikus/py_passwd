# Python password generator by @driconrikus
# Ver 0.1
import sys
import random

def generate_password():
    # Here is our pool where we will select the characters to create our password.
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e' ,'f' ,'g', 'h',
     'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'r', 's', 't',
      'u', 'v', 'x', 'y', 'z']
    symbols = ['!', '@', '#', '$', '%', '&', '*']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    characters = uppercase + lowercase + symbols + numbers

    # This variable will hold our password in a list format.
    password = []

    # This variable will ask how long our password will be, it will print a warning if it's below 8 characters.
    complexity = input('Please select password length:\n')
    if complexity.isnumeric() == False:
        print("Only numbers allowed.")
        sys.exit()
    else:
        if int(complexity) < 8:
            print('Warning: Minimum length for a secure password is 8 characters.')
    
    #This is where the magic happens
    for i in range(int(complexity)):
        character_random = random.choice(characters)
        password.append(character_random)
    
    password = "".join(password)
    return password

def run():
    password = generate_password()
    print('Your new password is: ' + password )


if __name__ == '__main__':
    run()