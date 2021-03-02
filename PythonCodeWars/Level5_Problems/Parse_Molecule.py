#Author:Esteban Acosta
# For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).

# For example:

# water = 'H2O'
# parse_molecule(water)                 # return {H: 2, O: 1}

# magnesium_hydroxide = 'Mg(OH)2'
# parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

# var fremy_salt = 'K4[ON(SO3)2]2'
# parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
# As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.


# Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.
import re
singleElementTokens = ("^[A-Z][a-z][0-9]+" , "^[A-Z][a-z]", "^[A-Z][0-9]+", "^[A-Z]")
multipleElementsTokens = ("^\[[A-Za-z0-9\(\)]+\][0-9]+", "^\[[A-Za-z0-9\(\)]+\]",
                          "^\([A-Za-z0-9]+\)[0-9]+", "^\([A-Za-z0-9]+\)", 
                         "^\{.+\}[0-9]+", "^\{.+\}")
tokens = singleElementTokens + multipleElementsTokens

def condenseFormula(token,substring, formula):
    chemGroupNum = 1
    endBracket = 0
    typeOfEndingBracket = ""
    chemGroup = ""
    
    if "\[" in token:
        typeOfEndingBracket = "]"
    elif "\(" in token:
        typeOfEndingBracket = ")"
    elif "\{" in token:
        typeOfEndingBracket = "}"
    
    endBracket = substring.index(typeOfEndingBracket)

    #Find any numerical values that come directly after the first occurance of the ending bracket
    m = re.match("^[0-9]+",substring[endBracket+1:])
    
   #if there is a match
    if m:
      #store the value
      chemGroupNum = int(m.group())

    #Make the substring smaller by cutting off the parenthesis that surround the chemical group
    substring = substring[1:endBracket]
    
    #loop through the chemical group                
    while len(substring) > 0:
        #loop through the tokens
        for token in tokens:
            #if there is a match between the token and the beginning of the substring
            match = re.match(token,substring)
            if match:
                if token in singleElementTokens:
                    #take apart the match by splitting it on the number of molecules
                    elementNameAndNum = re.split("([0-9]+)",match.group())
                
                    #if the match includes the element name and the # of molecules
                    if len(elementNameAndNum) > 1:
                        #add the element name, multiply the num of molecules outside of the brackets with 
                        #the num of molecules of the element and that to the string
                        chemGroup += elementNameAndNum[0] + str(chemGroupNum * int(elementNameAndNum[1]))
                    #if the match includes just the element name
                    else:
                        #add the element name and the number of molecules outside of the parenthesis
                        chemGroup += elementNameAndNum[0]  + str(chemGroupNum)
                    substring = substring[len(match.group()):]
                elif token in multipleElementsTokens:
                    substring = condenseFormula(token,substring[:len(match.group())],substring[len(match.group()):])
                break
    return chemGroup + formula
    

def parse_molecule (formula):   
    elements = {}
    count = 0
    i = 0
    print(formula)
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
