#Author:Esteban Acosta
#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(array):
    #create an empty list
    zeroAtEnd = []
    #create a counter
    countZeroes = 0
    #loop through each element in the original list
    for num in array:
       #if this element is zero and isn't a boolean
        if num == 0 and isinstance(num,bool) == False:
            #add one to the counter
            countZeroes+=1
            #skip to the next iteration
            continue
        #if this element is a regular element 
        else:
            #add it to the end of the new list
            zeroAtEnd.append(num)
    #create a list of zeroes with the size of the number of zeroes in the original list
    #and add that list of zeroes to the end of the new list
    zeroAtEnd.extend([0]*countZeroes)
    
    return zeroAtEnd
