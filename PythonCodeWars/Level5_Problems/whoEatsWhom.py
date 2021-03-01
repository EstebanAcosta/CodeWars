whoEats = {"antelope" : "grass",
        "big-fish": "little-fish",
        "bug" : "leaves",
        "bear" : ["big-fish","bug","chicken","cow","leaves","sheep"],
        "chicken" : "bug",
        "cow" : "grass",
        "fox" : ["chicken","sheep"],
        "giraffe" : "leaves",
        "lion" : ["antelope","cow"],
        "panda" : "leaves",
        "sheep" : "grass"       
    }

def canEatSomeMore(animals):
    #if there is only one animal or no animals left
    #return false (this animal can't be eaten nor can it eat other animals)
    if len(animals) <= 1:
        return False
    #if there is more than one animal in the list
    else:
        #loop through animals
        for i in range(len(animals)):     
            #if this position is between 1 and the last position 
            #and this animal can eat the animal before it
            #return true
            if i > 0 and canEat(animals[i],animals[i-1]):
                return True
            #if this position is between the first position and the second to last position
            #and this animal can eat the animal after it
            elif i < len(animals) - 1 and canEat(animals[i], animals[i+1]):
                return True
    return False

def canEat(predator,prey):
    #loop through the animal dictionary
    for key in whoEats.keys():
        #if the predator is in the dict and the prey is one of the preys this animal eats
        if key == predator and prey in whoEats[key]:
            return True
    return False   
        
def who_eats_who(zoo):
    #split the animals in the zoo by the comma
    animals = zoo.split(",")
    #create an empty list
    results = []
    #the animals in the zoo should be the first element
    results.append(zoo)
    #start the position at 0
    i = 0
    #continue looping until there's only one animal left
    while canEatSomeMore(animals) == True:
        #if we are at the end of the list
        if i >= len(animals):
            #make sure to start back to the beginning
            i = 0
            continue
        #if we aren't in the first position and the animal that comes before this animal
        #can eat this animal
        elif i > 0 and canEat(animals[i-1],animals[i]):
            #append which animal this animal ate
            results.append(animals[i-1] + " eats " + animals[i])
            #remove the eaten animal from the list of animals
            del animals[i]
            #make sure to be in the right position now that there's one less animal
            i-=1        
            continue
        #if we aren't in the first position and this animal can eat the animal before it
        elif i > 0 and canEat(animals[i],animals[i-1]):
            #append which animal this animal ate
            results.append(animals[i] + " eats " + animals[i-1])
            #remove the eaten animal from the list of animals
            del animals[i-1]
            #make sure to be in the right position now that there's one less animal
            i-=1        
            continue
        #if we aren't in the final position and this animal can at the animal after it
        elif i < (len(animals) - 1) and canEat(animals[i],animals[i+1]):
            #append which animal this animal ate
            results.append(animals[i] + " eats " + animals[i+1])
            #remove the eaten animal from the list of animals
            del animals[i+1]
            continue
        #if this animal can't eat anyone else
        else:
            #move to the next animal
            i+=1
    results.append(",".join(animals))
    return results