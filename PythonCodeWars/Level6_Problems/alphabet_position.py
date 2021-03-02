# Author: Esteban Acosta
#In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)


def alphabet_position(text):
    #create a dictionary where the key is the letter and the value is the letter's position in the alphabet
    #Dictionary comprehension explanation:
    #Loop 26 times (since there are 26 letters in the english alphabet)
    #Convert the first letter in the alphabet into ascii and add i to it in every iteration ord('a') + 1
    #Convert the ascii into a character and make it the key
    #Add 1 to i and convert it to a string and make that the value
    alphabet = {chr(ord('a') + i) : str((i+1)) for i in range(26)}
    
    #Make all the characters in the original string lowercase
    #Loop through each character in the string
    #If the character is a letter, look it up in the alphabet dictionary and append the value to the list
    #Create a string from the list by adding a white space in between each number
    return " ".join([alphabet[letter] for letter in text.lower() if letter.isalpha()])
        