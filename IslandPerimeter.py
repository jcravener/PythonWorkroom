
#LeetCode 463. Island Perimeter

def islandPerimeter(grid: [[int]]) -> int:

    if len(grid) == 0:
        return 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                size = getRegionSize(grid, r, c)
    return size, len(grid) * len(grid[r])

# -- This is a grid DFS
#
def getRegionSize(grid: [[int]], row: int, col: int):
    
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]):
        return 0
    if grid[row][col] == 0:
        return 0
    
    grid[row][col] = 0
    sz = 1

    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            if row != r or col != c:
                sz += getRegionSize(grid, r, c)
    return sz

g = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

print(islandPerimeter(g))