# #Author:Esteban Acosta
# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral 
#representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. 
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol 
# in descending order: MDCLXVI.

def solution(n):
    n = str(n)
    roman = ""
    romanNumerals= {   4 : "IV" ,   5 : "V" ,  9 : "IX", 1: "I" ,
                      40  : "XL",  90 : "XC" ,  10 : "X" ,  50 : "L",  900 : "CM", 
                      400 :  "CD" ,  100 : "C" ,  500 :"D",  1000 : "M"}
    
    #loop through each digit of the number
    for i in range(len(n)):
        #In each string, we're expanding the number based on the place is at
        #The first string, has the number at that position followed by a certain # of zeroes
        #if original num is 356, this expanded form is 300
        expanded = n[i] + "0" * (len(n) - (i + 1))
        #If the original num is 356, and the expandedForm is 300, this expandedForm is 100
        #The second string, has a 1 followed by a certain # of zeroes
        oneExpanded = "1" + "0" * (len(n) - (i + 1))
        #If the original num is 356, and the expandedForm is 300, this expandedForm is 500
        #The second string, has a 5 followed by a certain # of zeroes
        fiveExpanded = "5" + "0"* (len(n) - (i + 1))
        
        #if the number is in the dictionary
        if romanNumerals.get(int(expanded)) != None:
            roman+=(romanNumerals[int(expanded)])
            
        #if the first digit of the number is between 1 and 4
        elif int(n[i]) < 4 and int(n[i]) > 1:
            #Take the roman numeral of the expanded version of the number with the 1 as the first digit 
            #and multiply that by the first digit #
            #Ex: original num: 300 -> expanded v: 100 -> roman numeral of expanded: C*3
             roman+=(romanNumerals[int(oneExpanded)])*(int(n[i]))
                
        #if the first digit of the number 
        elif int(n[i]) > 5:
             #Take the roman numeral of the expanded version of the number with the 5 as the first digit 
            #then find out how many of the X's or C's needs to be added after the L or D and add that to the string
             roman+=romanNumerals[int(fiveExpanded)] + (romanNumerals[int(oneExpanded)])*(int(n[i]) - 5)
       
        #if the first digit of that number is a 0
        else:
             continue
                
    return roman