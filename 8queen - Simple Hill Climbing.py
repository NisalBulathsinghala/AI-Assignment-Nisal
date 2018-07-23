from __future__ import print_function
import random

def printBoard(board, cost): # Prints the given board combination and the H cost
    new_board = []
    for i in range(len(board)):
        new_board.append([i,board[i]])

    print(new_board)
    print()

    for i in range(len(board)):
        for j in range(len(board)):
            if [j,i] in new_board:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

    print('H =',cost)
    print()

def cost(board):    # Calculates the H cost for a given board combination
    h = 0
    for i in range(len(board)):
        for j in range(i+1,len(board)):
            if board[i] == board[j]:
                h += 1
            change = j - i
            if board[i] == board[j] - change or board[i] == board[j]+change:
                h += 1
    return h

def getNextMove(board): # Generates the next move of the queens
    stateList = []
    stateList.append([board, cost(board)])
    # Calculate the h cost of possible next moves
    for i in range(len(board)):
        for j in range(len(board)):
            board_2 = list(board)
            if board[i] == j:
                continue
            board_2[i] = j
            cost_2 = cost(board_2)
            stateList.append([board_2,cost_2])

    current_cost = cost(board)
    bestList = []
    # Filter out the best possible moves
    for row in stateList:
        if row[1] < current_cost:
            current_cost = row[1]

    for row in stateList:
        if current_cost == row[1]:
            bestList.append(row[0])

    # Select the first possible move from the list
    next_board = bestList[0]
    # Randomly select the next possible move
    # next_board = random.choice(bestList)
    return next_board

def main(): # The main function
    # Create the initial Board
    board_initial = [0, 0, 0, 0, 0, 0, 0, 0]
    cost_initial = cost(board_initial)
    printBoard(board_initial, cost_initial)
    condition = True

    # Loop until the heuristic cost function h is minimized and solution is achieved
    while condition == True:
        next_board = getNextMove(board_initial)
        # Checks whether a solution has been achieved
        if board_initial == next_board or cost_initial == cost(next_board):
            print('Solution')
            print()
            printBoard(board_initial, cost(board_initial))
            condition = False
            break
        else:
            board_initial = next_board
            cost_new = cost(board_initial)
            printBoard(board_initial, cost_new)

if __name__ == '__main__':
    main()
