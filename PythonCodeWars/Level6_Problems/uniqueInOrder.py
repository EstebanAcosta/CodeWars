#Author: Esteban Acosta
# Implement the function unique_in_order which takes as argument a sequence and 
#returns a list of items without any elements with the same value next to each other
# and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable):
    i = 0
    #create a list from the string
    iterable = [letter for letter in iterable]
    
    #loop through the list
    while i < len(iterable):
        #if the current position is less than the length of the list and
        #if the current element is equal to the next element
        if i < len(iterable) - 1 and iterable[i] == iterable[i+1]:
            #delete the next element
            del iterable [i+1]
        
        #if the current position is greater than 0 and
        #if the current element is equal to the previous element
        elif i > 0 and iterable[i] == iterable[i-1]:
            #delete the previous element
            del iterable[i-1]
            #subtract 1 to the current position to get the updated current position
            i-=1
        #if the elements to the left and right are not equal to the current element
        else:
            #move to the next position
            i+=1
        
    return iterable
 