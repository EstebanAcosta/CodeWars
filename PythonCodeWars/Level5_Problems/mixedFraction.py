# Author: Esteban Acosta
#Task
# Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format:

# [sign]a b/c

# where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c. 
# Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional part must be provided absolute).

# If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. 
# In both of these cases, the resulting string must not contain any spaces.

# Division by zero should raise an error (preferably, the standard zero division error of your language).

# Value ranges
# -10 000 000 < x < 10 000 000
# -10 000 000 < y < 10 000 000
# Examples
# Input: 42/9, expected result: 4 2/3.
# Input: 6/3, expedted result: 2.
# Input: 4/6, expected result: 2/3.
# Input: 0/18891, expected result: 0.
# Input: -10/7, expected result: -1 3/7.
# Inputs 0/0 or 3/0 must raise a zero division error.
# Note
# Make sure not to modify the input of your function in-place, it is a bad practice.

import math

def reduceFraction(num,denom):
    #continue looping until both numerator and denominator don't have a common denominator
    while math.gcd(num,denom) != 1:
        #get the greatest common denominator
        gcd = math.gcd(num,denom)
        #divide both numerator and denominator by the gcd
        num/=gcd
        denom/=gcd
        #Since the value comes back as a float, convert both vars to int
        num = int(num)
        denom = int(denom)
    #if the numerator and the denominator are positive or are both negative
    if num < 0 and denom < 0 or num > 0 and denom > 0:
        return str(abs(num)) + "/" + str(abs(denom))
    #if one of the two parts of the fraction is negative
    elif num < 0 or denom < 0:
        return "-" + str(abs(num)) + "/" + str(abs(denom))

def mixed_fraction(s):
    #split the string by the slash
    fraction = s.split("/")
    #Convert the first element and the second element of the string into an int and divide them
    #Convert the quotient into an integer
    whole = int(int(fraction[0])/int(fraction[1]))
    #Find the remainder of the numerator and denominator. Make sure to take the absolute value of both numerator and denominator
    remain = abs(int(fraction[0]))%abs(int(fraction[1]))
    
    #If this is an improper fraction
    if abs(int(fraction[0])) > abs(int(fraction[1])) and remain != 0:
        return str(whole) + " " +  reduceFraction(remain,abs(int(fraction[1])))
    
    #If this is a regular fraction
    elif abs(int(fraction[0])) < abs(int(fraction[1])) and remain != 0:
        return reduceFraction(int(fraction[0]),(int(fraction[1])))
    
    #If this isn't a fraction
    else:
        return str(whole)
