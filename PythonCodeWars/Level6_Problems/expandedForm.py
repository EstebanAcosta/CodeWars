#Author: Esteban Acosta
# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    #make the number a string
    num = str(num)

    #loop from the beginning of the string to the end
    #Take a string 1 and concatonate it with zeroes (the # of zeroes depends on what place the digit is at)
    #Turn that string of 1 and zeroes into an integer and multiply by the integer version of the current digit
    #Turn the product into a string
    #if the string isn't "0" then add it to the new list
    #Once the new list is created,  combine each element with a plus sign and turn it into a string

    return " + ".join(str(int(num[i]) * int("1"+("0"*(len(num) - (i + 1))))) for i in range(len(num)) if str(int(num[i]) * int("1"+("0"*(len(num) - (i + 1))))) != "0")