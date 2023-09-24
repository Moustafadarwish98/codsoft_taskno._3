"""Importing needed libraries."""
import random
from random import randint

"""Letters, Numbers and Symbols lists to be used in the password generation."""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def determining_password_length(limit):
    """Receiving user's required password length and making sure they enter a number greater
    than the specified lower limit depending on selected complexity."""
    is_not_a_number = True
    password_length = 0
    while is_not_a_number:
        while int(password_length) < limit:
            password_length = input(f"Enter desired password length"
                                    f" (not less than {limit} characters): ")
        password_length.split()
        for n in password_length:
            if n not in numbers:
                print("Invalid input, Please enter a number.")
                break
            else:
                is_not_a_number = False
                return int(password_length)


def password_structure(length, min_number_of_numbers, min_number_of_symbols):
    """Format the password structure according to selected complexity"""
    num_of_letters = randint(int(length / 2), length - (min_number_of_numbers + min_number_of_symbols))
    num_of_numbers = randint(min_number_of_numbers, length - num_of_letters - min_number_of_symbols)
    num_of_symbols = randint(min_number_of_symbols, length - (num_of_numbers + num_of_letters))
    num_of_letters = length - (num_of_numbers + num_of_symbols)
    generate_password(num_of_letters, num_of_numbers, num_of_symbols)


def generate_password(num_of_letters, num_of_numbers, num_of_symbols):
    """Using list comprehension create lists for letters,numbers and symbols appends them
    together, Then generates the password."""
    letters_list = [random.choice(letters) for x in range(num_of_letters)]
    numbers_list = [random.choice(numbers) for x in range(num_of_numbers)]
    symbols_list = [random.choice(symbols) for x in range(num_of_symbols)]
    password_list = letters_list + numbers_list + symbols_list
    random.shuffle(password_list)
    password = ''.join(password_list)
    print(f"Generated password: {password}")


is_valid = False
while not is_valid:
    complexity = input("Please choose password complexity (Normal, Complex, Extreme): ").lower()
    if complexity == "normal":
        minimum_number_of_characters = 7
        minimum_number_of_numbers = 2
        minimum_number_of_symbols = 1
        entered_length = determining_password_length(minimum_number_of_characters)
        password_structure(entered_length, minimum_number_of_numbers, minimum_number_of_symbols)
        is_valid = True

    elif complexity == "complex":
        minimum_number_of_characters = 10
        minimum_number_of_numbers = 3
        minimum_number_of_symbols = 2
        entered_length = determining_password_length(minimum_number_of_characters)
        password_structure(entered_length, minimum_number_of_numbers, minimum_number_of_symbols)
        is_valid = True

    elif complexity == "extreme":
        minimum_number_of_characters = 15
        minimum_number_of_numbers = 4
        minimum_number_of_symbols = 4
        entered_length = determining_password_length(minimum_number_of_characters)
        password_structure(entered_length, minimum_number_of_numbers, minimum_number_of_symbols)
        is_valid = True

    else:
        print("Invalid input.")







