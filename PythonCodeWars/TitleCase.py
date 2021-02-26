# A string is considered to be in title case if each word in the string is either (a) capitalised 
#(that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space.
#Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

# First argument (required): the original string to be converted.
# Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.

def title_case(title, minor_words=''):
    #take the title, split it on the whitespace that separates each word and store the new list into a var
    noSpacedTitle = title.split(" ")
    #take the minor words , split it on the white space that separates each word and store the new list into a var
    noSpacedMinorWords = minor_words.split(" ")
    #create an empty string
    newTitle = ""
    #loop through the new list
    for position in range(len(noSpacedTitle)):
        #if it's the first element in the list or if the word isn't in the list of minor words
        if position == 0 or not (noSpacedTitle[position].lower() in (word.lower() for word in noSpacedMinorWords)):
            #if we are not at the end of the list
            if position != len(noSpacedTitle) -1:
                #capitalize the first letter of the word, add a space to the end of the string and add the new string to the empty string
                newTitle+=noSpacedTitle[position].capitalize() + " "
            #if we are at the end of the list
            else:
                 #capitalize the first letter of the word and add the new string to the empty string
                newTitle+=noSpacedTitle[position].capitalize()
        #if it's any other element in the list and is a word that is in the list of minor words
        else:
             #if we are not at the end of the list
            if position != len(noSpacedTitle)  - 1:
                # make each letter in the word lowercase, add a space to the end of the string and add the new string to the empty string
                newTitle+=noSpacedTitle[position].lower() + " "
             #if we are at the end of the list
            else:
                 # make each letter in the word lowercase, and add the new string to the empty string
                newTitle+=noSpacedTitle[position].lower()
    return newTitle
