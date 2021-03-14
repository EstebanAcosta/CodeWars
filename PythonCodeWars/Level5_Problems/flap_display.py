def flap_display(lines, rotors):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789"
    
    for i in range(len(lines)):
        lines[i] = [letter for letter in lines[i]]
    
    for i in range(len(lines)):
            for j in range(len(rotors[i])):
                for k in range(j,len(lines[i])):
                    index = letters.index(lines[i][k])
                    l = 0
                    while l < rotors[i][j]:
                        if index + 1 >= len(letters):
                            index = 0
                        else:
                            index+=1  
                        l+=1
                    lines[i][k] = letters[index]
                
    return ["".join(word) for word in lines]
