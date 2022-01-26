# Given a set of moves, evaluate which player wins a game of connect four.

def evaluateRows(gameBoard):
    for i in range(6):
        for ii in range(4):
            if len(set(gameBoard[i][ii:ii+4])) == 1 and gameBoard[i][ii] != 0:
                return gameBoard[i][ii]
    return 0
    
def evaluateColumns(gameBoard):
    for i in range(7):
        currColumn = []
        for ii in range(6):
            currColumn.append(gameBoard[ii][i])
            if len(currColumn) > 4:
                currColumn.pop(0)
                
            if len(set(currColumn)) == 1 and currColumn[0] != 0 and len(currColumn) == 4:
                return gameBoard[ii][i]

    return 0

def evaluateDiagonal(gameBoard):
    for i in range(3):
        for ii in range(7):
            if gameBoard[i][ii] != 0 and ii < 4:
                gameBoardList = [gameBoard[i][ii], gameBoard[i+1][ii+1],
                                 gameBoard[i+2][ii+2], gameBoard[i+3][ii+3] ]
                if len(set(gameBoardList)) == 1:
                    return gameBoard[i][ii]

            if gameBoard[i][ii] != 0 and ii > 2:
                gameBoardList = [gameBoard[i][ii], gameBoard[i+1][ii-1],
                                 gameBoard[i+2][ii-2], gameBoard[i+3][ii-3] ]
                if len(set(gameBoardList)) == 1:
                    return gameBoard[i][ii]
    return 0
                     
                        


def who_is_winner(pieces_position_list):
    columnNames = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    gameBoard = [ [ 0,   0,   0,   0,   0,   0,   0 ], # Scoring on the board is as follows:
                  [ 0,   0,   0,   0,   0,   0,   0 ], #    0 if Empty
                  [ 0,   0,   0,   0,   0,   0,   0 ], #    1 if Yellow
                  [ 0,   0,   0,   0,   0,   0,   0 ], #   -1 if Red
                  [ 0,   0,   0,   0,   0,   0,   0 ],
                  [ 0,   0,   0,   0,   0,   0,   0 ] ]
    Winner = 0

    for idx, move in enumerate(pieces_position_list):
        currColumn = columnNames.index(move[0])
        currRow = 5
        
        # Find lowest non-empty row
        while gameBoard[currRow][currColumn] != 0:
            currRow -= 1  
        
        # Set score on board according to color
        gameBoard[currRow][currColumn] = 1 if move[2:] == "Yellow" else -1 
        
        # Check board for a four in a row
        Winner = (evaluateRows(gameBoard) or 
                  evaluateColumns(gameBoard) or
                  evaluateDiagonal(gameBoard) )
        if Winner:
            return "Yellow" if Winner == 1 else "Red"
    return "Draw" # Return Draw if game ended
                  #     without a winner


assert(who_is_winner(["A_Red", "B_Yellow", "A_Red", "E_Yellow",
                      "F_Red", "G_Yellow", "A_Red", "G_Yellow"]) == "Draw")
assert(who_is_winner(["A_Red", "B_Yellow", "A_Red", "B_Yellow",
                      "A_Red", "B_Yellow", "G_Red", "B_Yellow"]) == "Yellow")
