# STRONG PASSWORD GENERATOR
# Author: Valeriy B.
# Language: Python 3.8.5

import random

# password generator function logic
def generator(arr):

    # initiating a count variable
    count = arr[0] - sum([1 for i in arr[1:] if i.lower() == "y"])
    
    # creating symbols list
    symbols = [chr(i) for i in range(33, 48)]
    symbols_l = random.sample(symbols, 1)

    # creating numbers list
    numbers = [chr(i) for i in range(48, 58)]
    numbers_l = random.sample(numbers, 1)

    # crating lowercase letters list
    lowers = [chr(i) for i in range(97, 123)]
    lowers_l = random.sample(lowers, count)

    # creating uppercase letters
    uppers = [chr(i) for i in range(65, 91)]
    uppers_l = random.sample(uppers, 1)

    # creating generated password list
    password_generator = lowers_l 
    if arr[1].lower() == "y":
        password_generator += symbols_l
    if arr[2].lower() == "y":
        password_generator += numbers_l
    if arr[3].lower() == "y":
        password_generator += uppers_l
    
    # arrenging list randomly
    random.shuffle(password_generator)
    
    return "Generated password: " + "".join(password_generator)    

print("Password generator")

# user inputs
pswd_length = int(input("Password length: "))
pswd_symbols = input("Include symbols (Y, N) (e.g. @#$%): ")
pswd_numbers = input("Include numbers (Y, N) (e.g. 123456): ")
pswd_uppercase = input("Include uppercase letters (Y, N) (e.g. ABCDEF): ")

pswd_list = [pswd_length, pswd_symbols, pswd_numbers, pswd_uppercase]

print(generator(pswd_list))