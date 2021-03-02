#author: Esteban Acosta
# Introduction
# A multi-storey car park (also called a parking garage, parking structure, parking ramp, parkade, 
#parking building, parking deck or indoor parking) is a building designed for car parking and where 
#there are a number of floors or levels on which parking takes place. It is essentially an indoor, 
#stacked car park. Parking structures may be heated if they are enclosed.
# Design of parking structures can add considerable cost for planning new developments, and can be mandated by cities or states in new building parking requirements. Some cities such as London have abolished previously enacted minimum parking requirements (Source Wikipedia)

# Task
# Your task is to escape from the carpark using only the staircases provided to reach the exit. You may not jump over the edge of the levels (you’re not Superman!) and the exit is always on the far right of the ground floor.
# Rules
# 1. You are passed the carpark data as an argument into the function.

# 2. Free carparking spaces are represented by a 0

# 3. Staircases are represented by a 1

# 4. Your parking place (start position) is represented by a 2 which could be on any floor.

# 5. The exit is always the far right element of the ground floor.

# 6. You must use the staircases to go down a level.

# 7. You will never start on a staircase.

# 8. The start level may be any level of the car park.

# 9. Each floor will have only one staircase apart from the ground floor which will not have any staircases.
# Returns
# Return an array of the quickest route out of the carpark

# R1 = Move Right one parking space.

# L1 = Move Left one parking space.

# D1 = Move Down one level.
# Example
# Initialise
# carpark = [[1, 0, 0, 0, 2],
#            [0, 0, 0, 0, 0]]
# Working Out
# - You start in the most far right position on level 1
# - You have to move Left 4 places to reach the staircase => "L4"
# - You then go down one flight of stairs => "D1"
# - To escape you have to move Right 4 places => "R4"
# Result
# result = ["L4", "D1", "R4"]

def escape(carpark):
    startLevel = 0
    escape = []
    #loop through each level of the carpark
    for eachLevel in range(len(carpark)):
        #if your car is parked in this level
        if 2 in carpark[eachLevel]:
            #store the level and break
            startLevel = eachLevel
            break
    
    #find the position your car is at
    yourPosition = carpark[startLevel].index(2)
    stairPosition = 0
    
    #loop through each level of the carpark starting from the level your car is at
    for eachLevel in range(startLevel,len(carpark)):
        #if this level isn't the ground floor
        if eachLevel < len(carpark) - 1:
            #get the position of the staircase on that level
            stairPosition = carpark[eachLevel].index(1)
            #if your position is to the left of the staircase position
            if yourPosition < stairPosition:
                escape.append("R" + str(stairPosition - yourPosition))
                escape.append("D1")
            #if your position is to the right of the staircase position
            elif yourPosition > stairPosition:
                escape.append( "L" + str(yourPosition - stairPosition))
                escape.append("D1")
            #if your position happens to be in the same spot of the staircase
            else:
                #get the last direction (the last direction had to be a D direction)
                downDirection = escape[len(escape) - 1]
                #remove it from the list
                del escape[len(escape) - 1]
                #take apart the last direction
                #string together the D and add one to the number of times you went down the stairs
                escape.append(downDirection[0] + str(int(downDirection[1]) + 1))
            #make your position the stair position on that floor
            yourPosition = stairPosition
        
        #if we are on the ground floor
        else:
            #get the exit position
            exitPosition = len(carpark[eachLevel]) - 1 
            #if you are to the left of the exit 
            if yourPosition < exitPosition:
                escape.append("R" + str(exitPosition - yourPosition))
    return escape
    