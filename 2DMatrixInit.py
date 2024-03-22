#Init 2D Matrix (Functions)

rows = int(input("How many rows? :"))
cols = int(input("How many columns? :"))

def createMatrix(rows: int, cols: int):
    resultMatrix = [[0 for j in range(cols)] for i in range(rows)]

    count = 0
    for i in range(rows):
        for j in range(cols):
            resultMatrix[i][j] = count
            count += 1
            
    return resultMatrix
    
def print2dMatrix(YourMatrix: list, rows: int, cols: int):
    for i in range(rows):
        for j in range(cols):
            print(f"{YourMatrix[i][j]:2d}", end=' ')
        print('')

Matrix2D = createMatrix(rows, cols)
print2dMatrix(Matrix2D, rows, cols)