# Create a program to receive a two digit number from the user and do a sum of the digits.
# Example: input -> 23 : output -> 5

number = input("Enter a number of two digits only\n")
result = int(number[0]) + int(number[1])
print(f"The sum of this two digit number is: {result}")

