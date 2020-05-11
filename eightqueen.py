## what is the heuristic for eight queen problem?, the number of pair of queens attacking each other
## what are the next states? choose two queens to swap the place in order to find the board with lower cost

## drawback, we may only get to the local optimality, so we can't get the board . To solve this problem, we have
## to restart the algorithm, to make the board to localize the position with global  optimality.

import random

def cost(board):
    costsum = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if abs(j - i) == abs(board[j] - board[i]):
                costsum += 1

    return costsum

def climb(board):
    curcost = cost(board)

    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            newboard = board[:]
            newboard[i], newboard[j] = newboard[j], newboard[i]

            nextcost = cost(newboard)
            if nextcost < curcost:
                return newboard

    return None


def init():
    board = [i  for  i in range(8)]

    random.shuffle(board)
    return board
def hillClimb():

    board = init()
    while  True:
        nextboard = climb(board)
        if nextboard != None:
            printBoard(nextboard)
        if nextboard == None:
            print "can find the eight queen"
            return None
        else:
            curcost = cost(nextboard)
            if curcost == 0:
                print "find the eight queen"
                return nextboard

        board = nextboard

    print "no eight queen"
    return None

def printBoard(board):
    matrix = [[0 for j in range(8)] for i in range(8)]

    for col, row in enumerate(board):
        matrix[row][col] = 1

    for i in range(len(matrix)):
        print matrix[i]

    print "\n"
if __name__ == "__main__":
    ans = hillClimb()

    print ans



