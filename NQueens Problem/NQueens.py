# Savannah Rimmele
# AI & Heuristics Project 1

import pandas as pd 

csvFile = pd.read_csv("input.csv", header = None)
matrix = csvFile.values.tolist()

N = len(matrix)

#Board is nxn size
# print("Board Size is " + str(N) + "x" + str(N))
#There are N Queens on the board
# print("Number of Queens: ", N, "\n")

# print("BOARD: ")
# for i in matrix: 
#     for j in i: 
#         print(j, end=" ")
#     print()

def getSolution(matrix): 
#Determine the First Queen's Position
    FirstQueenCol = -1
    for i in range(0, N): 
        for j in range(0, N):
            if(matrix[i][j] == 1): 
                FirstQueenCol = j

    if nQueen(matrix, FirstQueenCol, FirstQueenCol, 1) == False: 
        print("Solution DNE!")
        return False
    else: 
        # print("\n")
        # print("UPDATED BOARD: ")
        # for i in matrix: 
        #     for j in i: 
        #         print(j, end=" ")
        #     print()
        solution = pd.DataFrame(matrix)
        solution.to_csv('solution.csv', index = False, na_rep = 'Unkown', header = None)
        return True

#Place the next Queen
def nQueen(matrix, column, queenCol, numQueens):  
    #Check if all queens have been placed
    if numQueens >=N:
        return True
    else:
        numQueens = numQueens + 1

    #Start in the next column from where the starting queen is
    if column == queenCol:
        column = column + 1

    #Once the end of the board is reached, reset position to 0
    if column == N:
        column = 0
        
    for i in range(0, N):   
        #Check if the Queens are a threat to each other
        if isSafe(matrix, i, column) == True:
            #Place Queen onto the board 
            matrix[i][column] = 1
            #Perform recursion
            if (nQueen(matrix, column + 1, queenCol, numQueens) == True): 
                return True
            #Otherwise, Backtrack
            matrix[i][column] = 0

    return False


def isSafe(matrix, row, column): 
    #Check if the placed Queen can be attacked
    #No Two Queens can be in the Row
    for i in range(N):
        if i != column:
            if matrix[row][i] == 1:
                return False
    
    #Check upper diagonal on the left (Using Dr. Duan's Grading Program)
    for i, j in zip(range(row-1, -1, -1), range(column-1, -1, -1)):
        if matrix[i][j] == 1:
            return False

    #Check lower diagonal on the left (Using Dr. Duan's Grading Program)
    for i, j in zip(range(row+1, N, 1), range(column-1, -1, -1)):
        if matrix[i][j] == 1:
            return False

    #Now perform the above methods on the right 
    #Check upper diagonal on the right 
    for i, j in zip(range(row-1, -1, -1), range(column+1, N, 1)):
        if matrix[i][j] == 1:
            return False

    #Check lower diagonal on the right
    for i, j in zip(range(row+1, N, 1), range(column+1, N, 1)):
        if matrix[i][j] == 1:
            return False  
            
    return True

def main(): 
    getSolution(matrix)        

if __name__ == '__main__': 
    main()

