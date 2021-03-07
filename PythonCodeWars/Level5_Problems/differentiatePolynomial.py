#Author: Esteban Acosta
# Create a function that differentiates a polynomial for a given value of x.

# Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer.

# Assumptions:
# There will be a coefficient near each x, unless the coefficient equals 1 or -1.
# There will be an exponent near each x, unless the exponent equals 0 or 1.
# All exponents will be greater or equal to zero
# Examples:
# differenatiate("12x+2", 3)      ==>   returns 12
# differenatiate("x^2+3x+2", 3)   ==>   returns 9


import re
def differentiate(equation, point):
    eq = re.split("(\+|\-)",equation)
    differentiated = ""
    for i in range(len(eq)):
        if eq[i] == "-" :
            eq[i+1] = "-" + eq[i+1]
        elif "^" in eq[i]:
            term = ""
            caret = eq[i].index("^")
            x = eq[i].index("x")
            if eq[i][:x] == '-':
                x = "-1"
            elif eq[i][:x] == '':
                x = "1"
            else:
                x = eq[i][:x]
            term = str(int(eq[i][caret + 1:]) * int(x)) + "*x" + str(int(eq[i][caret+1:]) - 1 )
            differentiated += term + "+"
                
        elif "x" in eq[i]:
            x = eq[i].index("x")
            if eq[i][:x] == '-':
                x = "-1"
            elif eq[i][:x] == '':
                x = "1"
            else:
                x = eq[i][:x]
            differentiated+=x
    if differentiated[len(differentiated) - 1] == "+":
        differentiated = differentiated[:len(differentiated) - 1] 

    return eval(differentiated.replace("x", "(" + str(point) + ")" + "**"))