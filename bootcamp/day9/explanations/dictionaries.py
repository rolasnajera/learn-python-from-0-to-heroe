# is like reald dictionary to look for the definition of a word
# key - value pair
# {key: value}
# { "bug": "Is an error in the code." }
# { "bug": "Is an error in the code.", "function }

programming_dictionary = {
        "bug": "An issue within the code.",
        "function": "It is used to reutilize code."
}

print(programming_dictionary["bug"])

# adding a new item
programming_dictionary["loop"] = "used to traverse."


# edit an item
programming_dictionary["bug"] = "could be an animal in code."

print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# create an empty dictionary
empty_dictionary = {}


# wipe a dictionary
programming_dictionary = {}
print(programming_dictionary)


