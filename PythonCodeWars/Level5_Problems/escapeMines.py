def solve(map, miner, exit):
    moves = []
    currentX = miner['x']
    currentY = miner['y']
    
    while currentX != exit['x'] or currentY != exit['y']:
        if abs((currentY + 1) - exit['y']) < abs((currentY - 1) - exit['y']) and currentY < len(map[currentX]) - 1 and map[currentX][currentY + 1] == True:
                moves.append("down")
                currentY+=1
        
        elif abs((currentY - 1) - exit['y']) < abs((currentY + 1) - exit['y']) and currentY > 0 and map[currentX][currentY - 1] == True:
            moves.append("up")
            currentY-=1
            
        elif abs((currentX + 1) - exit['x']) < abs((currentX - 1) - exit['x']) and currentX < len(map) - 1 and map[currentX + 1][currentY] == True:
            moves.append("right")
            currentX+=1
            
        elif abs((currentX - 1) - exit['x']) < abs((currentX + 1) - exit['x']) and currentX > 0 and map[currentX - 1][currentY] == True:
            moves.append("left")
            currentX-=1
    return moves