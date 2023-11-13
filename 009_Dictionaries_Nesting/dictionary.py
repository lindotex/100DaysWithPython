programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from a dictionary:
# print(programming_dictionary) # Will print the dictionary at the screen

# Adding a new entry at the dictionary
programming_dictionary["Loop"] = "The action of doing something receptively"

# print(programming_dictionary) # Will return with the new key: Loop

# Empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary) # Will return nothing

# Edit an item in a dictionary:
programming_dictionary["Bug"] = "Bug has been edited."
# print(programming_dictionary) # Will return with the key "bug" edited


# Loop through a Dictionary:
for key in programming_dictionary:
    print(f"{key} : {programming_dictionary[key]}")