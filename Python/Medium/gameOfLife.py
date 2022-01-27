def isInBoard(x, y, xMax, yMax):
    if x >= xMax or x < 0:
        return False
    if y >= yMax or y < 0:
        return False
    return True

def nextGen(cells):

    # Check for empty array
    if len(cells) == 0:
        return cells
    
    cellsHeight = len(cells)     # The cells array is assumed to be a 
    cellsWidth  = len(cells[0])  #   a regular shape (rectangle / square) 
                                

    # Create an empty list with dimensions of cells,
    #   as the changes happen simultaneously
    nextGenCells = [[0 for x in range(cellsWidth)] for y in range(cellsHeight)]
    
    for i in range(cellsHeight):
        for ii in range(cellsWidth):
            radius = 1
            neighborSum = 0

            # Loop through possible neighbor coordinates, if valid add value to neighborValue
            for neighborX in range(-radius, radius + 1):
                for neighborY in range(-radius, radius + 1):
                    if isInBoard(i+neighborX, ii+neighborY, cellsHeight, cellsWidth):
                        neighborSum += cells[i+neighborX][ii+neighborY]

            # Subtract value of the cell checked, as it's included in the range
            neighborSum -= cells[i][ii]

            # Update cells according to the rules
            if cells[i][ii] and 2 <= neighborSum <= 3:                
                nextGenCells[i][ii] = 1
            elif cells[i][ii] and (neighborSum >= 3 or neighborSum == 0):
                nextGenCells[i][ii] = 0
            elif not cells[i][ii] and neighborSum == 3:
                nextGenCells[i][ii] = 1

    return nextGenCells

assert( nextGen(  [ [0,1,0],
                    [0,1,0],
                    [0,1,0] ]) 
                    
                == [[0,0,0],
                    [1,1,1],
                    [0,0,0] ]) 

