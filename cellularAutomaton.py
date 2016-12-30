print("Press enter to see the next step in the matrix design. Press ctrl+C to quit.")

# Dimensions of the matrix
matrixRows = 8
matrixCols = 8

# The 8 "supercells" surrounding the matrix (None is the matrix supercell itself)
# These numbers can be changed to create different patterns in the supercell. The "None" element represents the supercell on the screen. Changing it will have no effect.
seed = [[0,0,0],[0,None,0],[0,0,0]]

matrix = []  # The cellular matrix to work with

# Calulates the values of the cells surrounding (and including) the given cell to find the value of the given cell
def calculateSurrCells(row,col):
    cellValues = []  # the cells needed to calculate the current matrix cell value
    
    prevCol = col-1
    prevRow = row-1
    nextCol = col+1
    nextRow = row+1
    
    sumOfCells = 0
    
    for rowIndex in [prevRow,row,nextRow]:
        for colIndex in [prevCol,col,nextCol]:
            if rowIndex < 0:
                if colIndex < 0:
                    sumOfCells += seed[0][0]
                elif colIndex >= matrixCols:
                    sumOfCells += seed[0][2]
                else:
                    sumOfCells += seed[0][1]
            elif rowIndex >= matrixRows:
                if colIndex < 0:
                    sumOfCells += seed[2][0]
                elif colIndex >= matrixCols:
                    sumOfCells += seed[2][2]
                else:
                    sumOfCells += seed[2][1]
            else:
                if colIndex < 0:
                    sumOfCells += seed[1][0]
                elif colIndex >= matrixCols:
                    sumOfCells += seed[1][2]
                else:
                    sumOfCells += matrix[rowIndex][colIndex]  # seed[1][1] is the matrix, so it's safe to check the matrix itself for the data
    
    #return 1 if an even number of cells around the location, 0 if otherwise.
    return ((sumOfCells % 2) - 1)*(-1)

# Copy the matrix safely
def copyMatrix(mat):
    newMatrix = []
    for row in range(0,len(mat)):
        newMatrix.append([])
        for col in range(0,len(mat[row])):
            newMatrix[row].append(mat[row][col])
    return newMatrix

# Create the matrix (and fill with zeroes)
for row in range(0,matrixRows):
    matrix.append([])
    for col in range(0,matrixCols):
        matrix[row].append(0)
        
while 1:
    input()  # advance a step when the user hits enter
    nextMatrix = copyMatrix(matrix)  # copy the matrix
    for row in range(0,matrixRows):
        for col in range(0,matrixCols):
            nextMatrix[row][col] = calculateSurrCells(row,col)  # iterate over the cells and updates them into a new matrix
    matrix = copyMatrix(nextMatrix)  # overwrite the original matrix with the next iteration
    
    #display the cells ("-" means 0, "#" means 1)
    for y in range(0,matrixRows):
        string = ""
        for x in range(0,matrixCols):
            if matrix[y][x] == 0:
                string += "- "
            else:
                string += "# "
        print(string)
