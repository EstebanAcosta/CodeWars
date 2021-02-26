# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
# which is the number of times you must multiply the digits in num until you reach a single digit.
# For example:
# persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        # and 4 has only one digit.

# persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
#                        # 1*2*6 = 12, and finally 1*2 = 2.

# persistence(4) => 0   # Because 4 is already a one-digit number

def persistence(n):
    #turn the number into a string
    persist = str(n)
    #create a variable that will count the number of iterations
    count = 0
    #continue looping until the product of the digits in persist is of length one (essentially if persist has only one digit stop looping)
    while len(persist) != 1:
        #create a variable that will hold the product
        product = 1
        #loop through each character in the string
        for digit in persist:
            #multiply the digits together and store it in product
            product*=int(digit)
        #add one to the # of iterations
        count+=1
        #convert the product into a string and store it in persist
        persist = str(product)
    return count

