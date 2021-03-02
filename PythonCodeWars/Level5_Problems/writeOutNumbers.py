#Author: Esteban Acosta

# Create a function that transforms any positive number to a string representing the number in words. The function should work for all numbers between 0 and 999999.

# number2words(0)  ==>  "zero"
# number2words(1)  ==>  "one"
# number2words(9)  ==>  "nine"
# number2words(10)  ==>  "ten"
# number2words(17)  ==>  "seventeen"
# number2words(20)  ==>  "twenty"
# number2words(21)  ==>  "twenty-one"
# number2words(45)  ==>  "forty-five"
# number2words(80)  ==>  "eighty"
# number2words(99)  ==>  "ninety-nine"
# number2words(100)  ==>  "one hundred"
# number2words(301)  ==>  "three hundred one"
# number2words(799)  ==>  "seven hundred ninety-nine"
# number2words(800)  ==>  "eight hundred"
# number2words(950)  ==>  "nine hundred fifty"
# number2words(1000)  ==>  "one thousand"
# number2words(1002)  ==>  "one thousand two"
# number2words(3051)  ==>  "three thousand fifty-one"
# number2words(7200)  ==>  "seven thousand two hundred"
# number2words(7219)  ==>  "seven thousand two hundred nineteen"
# number2words(8330)  ==>  "eight thousand three hundred thirty"
# number2words(99999)  ==>  "ninety-nine thousand nine hundred ninety-nine"
# number2words(888888)  ==>  "eight hundred eighty-eight thousand eight hundred eighty-eight"

onesPlace = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four" , 5 : "five", 6 : "six", 7 : "seven", 8 : "eight",  9 : "nine"}

tensPlace = { 10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen",
             18 : "eighteen", 19 : "nineteen", 20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty",60 : "sixty",70 : "seventy",
             80 : "eighty", 90 : "ninety"}

def number2words(n):
    n = str(n)
    stringOfNum = ""  
    i = 0
    #continue looping until there are no more digits left
    while len(n) > 0: 
        #if the number only has one digit and the number is in the onesPlace dictionary
        if len(n) == 1 and int(n) in onesPlace:
                #add the name for that digit to the string
                stringOfNum += onesPlace[int(n)]
                break
                
        #if the number has two digits
        elif len(n) == 2:
            #if the current digit has a zero
            if n[i] == "0":
                #move to the next digit
                n = n[i+1:]
                continue
            #if the number is in the tens places dictionary
            if int(n) in tensPlace:
                #add the name for that portion of the number to the string
                stringOfNum += tensPlace[int(n)]
                break
            #if replacing the last digit of the number with a zero gets us a number
            #that belongs to the tensPlace dictionary (here we are trying to see if
            #the ten place digit corresponds to any of the tens place numbers in the dictionary)
            elif int(n[i] + "0") in tensPlace:
                #add the name for that portion of the number to the string followed by a dash
                stringOfNum += tensPlace[int(n[i] + "0")] + "-"
            #move on to the next digit of the string
            n = n[i+1:]
            
        #if the number has three digits        
        elif len(n) == 3:
            #and the first digit of the three digit number is a 0
            if n[i] == "0":
                #move to the next digit
                n = n[i+1:]
                continue
            
            stringOfNum+= onesPlace[int(n[i])] + " hundred"
            
            #if the rest of the string has zeroes
            if n[i+1:] == "00":
                break
            #otherwise
            else:
                #add a space
                stringOfNum += " "
                #and move to the next digit
                n = n[i+1:]   
                
        #if the number has four digits
        elif len(n) == 4:
            #if the current digit is a zero 
            if n[i] == "0":
                #just add thousand to the string
                stringOfNum+= "thousand"
            #if the current is a non zero digit
            else:
                #add the digit name followed by thousand
                stringOfNum+= onesPlace[int(n[i])] + " thousand"
            
            #if the rest of the string is filled with zeroes
            if n[i+1:] == "000":
                break
            else:
                #move to the next digit
                n = n[i+1:]
            stringOfNum += " "   
            
        #if the numer has five digits
        elif len(n) == 5:
            #if the first two digits of the five digit number is a number that can be found in tensPlace dictionaru
            if int(n[i:i+2]) in tensPlace:
                #add the name that represents those two digits followed by thousand to the string
                stringOfNum+= tensPlace[int(n[i:i+2])] + " thousand" + " "
                #if the rest of the string is filled with zeroes
                if n[i+2:] == "000":
                    break
                #move to the hundreds place of the number
                n = n[i+2:]
            #if the 1st 2 digits can't be found in the dictionary
            else:
                #if replacing the last digit of the number with a zero gets us a number
                #that belongs to the tensPlace dictionary (here we are trying to see if
                #the ten place digit corresponds to any of the tens place numbers in the dictionary)
                stringOfNum+= tensPlace[int(n[i] + "0")] + "-"
                #move to the next digit
                n = n[i+1:]
       
        #if the number has six digits
        else:
            #if the next digit is a zero
            stringOfNum+= onesPlace[int(n[i])] + " hundred "
            if n[i+1] == "0" :
                #move two places to the right (gets us to the thousand place)
                n = n[i+2:] 
            else:    
                #otherwise move to the next place(gets us to the ten thousand place)
                n = n[i+1:]
    
    return stringOfNum