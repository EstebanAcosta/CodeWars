import re
singleElementTokens = ("^[A-Z][a-z][0-9]+" , "^[A-Z][a-z]", "^[A-Z][0-9]+", "^[A-Z]")
multipleElementsTokens = ("^\[.+\][0-9]+", "^\[.+\]", "^\(.+\)[0-9]+", "^\(.+\)", "^\{.+\}[0-9]+", "^\{.+\}", )
tokens = singleElementTokens + multipleElementsTokens

def condenseFormula(token,substring, formula):
    end = 0
    print(substring)
    
    elementGroupAndNum = re.split("([0-9]+)",substring)
    
    elementNum = 1
    
    if len(elementGroupAndNum) > 1:
         elementNum = int(elementGroupAndNum[1])
    
    endBracket = 0
    
    for i in range(len(substring)):
        if substring[i] == ")" or substring[i] == "]" or substring[i]  == "}":
            endBracket = i
            break
    
    substring = substring[1:endBracket]
    
    print(substring)
            
   
    #return substring + formula
    

def parse_molecule (formula):   
    elements = {}
    count = 0
    i = 0
    #continue looping until the formula is empty
    while len(formula) > 0:
        #loop through each token in the list of tokens
        for i in range(len(tokens)):
            match = re.match(tokens[i],formula)     
            #if there is a match
            if match:
                # if the token that matches with the formula is just the element name and/or the number of molecules
                if tokens[i] in singleElementTokens:          
                    #Take the match and split it based on the number
                    elementNameAndNum = re.split("([0-9]+)",match.group())
                    
                    #if there is a number at the end of the match
                     #and the element is in the list of elements   
                    if len(elementNameAndNum) > 1 and elementNameAndNum[0] in elements:
                             #make the element name (which is stored as the first element) the key 
                            #and make the molecule number (which is stored as the second element) the value
                            #add the number of molecules of this element to the value
                            elements[elementNameAndNum[0]] += int(elementNameAndNum[1])
                            
                    #if the element isn't in the list of elements
                    elif len(elementNameAndNum) > 1 and elementNameAndNum[0] not in elements:
                            #make the element name (which is stored as the first element) the key 
                            #and make the molecule number (which is stored as the second element) the value
                            #set the number of molecules of this element to the value
                            elements[elementNameAndNum[0]] = int(elementNameAndNum[1])
                    
                    #if there isn't a number at the end of the match
                    # and the element is in the list of elements
                    elif len(elementNameAndNum) == 1 and elementNameAndNum[0] in elements:
                        #make the element name (which is stored as the first element) the key 
                        #and since there isn't a second element make 1 the value. Since
                        #this is the first element being added to the elements, add 1 more to the value
                        elements[elementNameAndNum[0]] += 1
                    
                    #if there isn't a number at the end of the match
                    #and the element isn't in the list of elements
                    elif len(elementNameAndNum) == 1 and elementNameAndNum[0] not in elements:
                        #make the element name (which is stored as the first element) the key 
                        #and since there isn't a second element make 1 the value. Since the
                        #this isn't the first element being added to the elements, set the value to 1
                        elements[elementNameAndNum[0]] = 1
                    
                    #move to the next element or element group in the formula
                    formula = formula[len(match.group()):]   
                    
                # if the token that matches with the formula is just a group of elements
                elif tokens[i] in multipleElementsTokens:
                    formula = condenseFormula(tokens[i],formula[:len(match.group())] , formula[len(match.group()):])
                break
    return elements
 