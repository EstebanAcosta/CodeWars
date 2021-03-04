#Author: Esteban Acosta
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
# The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. 
# Furthermore, the input string may be empty and/or not contain any parentheses at all. 
# Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

def valid_parentheses(string):
    #Remove every character from the string but the left paren and right paren
    string = [letter for letter in string if letter == "(" or letter == ")"]
    
    #continue looping until string is emptu
    while len(string) > 0:
        #if there's a left paren and right paren in the string
        if "(" in string and ")" in string:
            #and the first occurance of the left paren comes before
            #the first occurance of the right paren
            if string.index("(") < string.index(")"):
                #remove the left and right paren
                string.remove("(")
                string.remove(")")
            #if the 1st occurance of right parens comes before the 
            #the 1st occurance of the left paren
            else:
                 break
        #if there are no left parens or right parens in the string
        else:
            break

    #if we were successfuly able to match each left paren with 
    #its corresponding right paren the length of the string should be 0
    #that's because we should have removed each match from the string
    return len(string) == 0