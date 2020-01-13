
def isToeplitzMatrix(matrix: [[int]]) -> bool:
    if len(matrix) == 0:
        return False

    rowrange = len(matrix) - 1
    colrange = len(matrix[0]) - 1

    for i in range(rowrange):
        for j in range(colrange):
            if matrix[i][j] != matrix[i+1][j+1]:                
                return False
                
    return True

m = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
print(isToeplitzMatrix(m))

print()
m = [
  [1,2],
  [2,2]
]
print(isToeplitzMatrix(m))
