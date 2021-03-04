def super_street_fighter_selection(fighters, position, moves):
    position = list(position)
    print(position)
    characters = []
    print(moves)
    for move in moves:
        if move == "up":
            if position[0] <= len(fighters) and position[0] != 0:
                while fighters[position[0] - 1][position[1]] != " ":
                      position[0]-=1
            
        elif move == "down":
            if position[0] >= 0 and position[0] != len(fighters) - 1:
                 if fighters[position[0] + 1][position[1]] != "":
                    position[0]+=1
                    
        elif move == "right":
            if position[1] == (len(fighters[position[0]]) - 1):
                if fighters[position[0]][0] != "":
                    position[1] = 0
                else:
                    position[1] = 1
            else:
                if fighters[position[0]][position[1]+1] != "":
                    position[1]+=1
                else:
                    if position[1] + 2 <= len(fighters[position[0]])-1:
                        position[1]+=2
                    else:
                        position[1] = 0
        else:
            if position[1] == 0:
                if fighters[position[0]][(len(fighters[position[0]]) - 1)] != "":
                    position[1] = (len(fighters[position[0]]) - 1)
                else:
                    position[1] = (len(fighters[position[0]]) - 2)
            else:
                if fighters[position[0]][position[1]-1] != "":
                    position[1]-=1
                else:
                    if position[1] - 2 >= 0:
                        position[1]-=2
                    else:
                        position[1] = len(fighters[position[0]])-1
        characters.append(fighters[position[0]][position[1]])     
    return characters