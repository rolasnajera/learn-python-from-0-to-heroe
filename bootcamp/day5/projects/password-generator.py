# Create a program that generates randome passwords
# Ask to the user if they want to add simbols, and the lenght of the password.
import random
letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
          "v", "w", "x", "y", "z"] # 24
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 10
symbols = ["%", "#", "!", "?", ")", "(", "&", "$", "*"] # 9
print("Welcome to the password generator!")
letters_size = int(input("How many letters do you want in your password?:   "))
numbers_size = int(input("How many numbers do you want in your password?:   "))
symbols_size = int(input("How many symbols do you want in your password?:   "))
password_length = letters_size + numbers_size + symbols_size
password = ""
for _ in range(letters_size):
    idx = random.randint(0, len(letters) - 1)
    password += letters[idx]

for _ in range(numbers_size):
    idx = random.randint(0, len(numbers) - 1)
    password += str(numbers[idx])

for _ in range(symbols_size):
    idx = random.randint(0, len(symbols) - 1)
    password += symbols[idx]

#  l o 3 4 % $
# random 
# 4
list_password = list(password)
random_password = ""
for number in reversed(range(password_length)):
    idx = random.randint(0, number)
    random_password += list_password.pop(idx)

print(random_password)
