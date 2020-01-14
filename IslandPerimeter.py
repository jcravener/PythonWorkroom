
#LeetCode 463. Island Perimeter

def islandPerimeter(grid: [[int]]) -> int:

    if len(grid) == 0:
        return 0
    
    perim = 0

    #--count bit=flips, row by row
    for i in range(len(grid)):
        cur_bit_val = 0
        for j in range(len(grid[i])):
            if grid[i][j] != cur_bit_val:
                cur_bit_val = grid[i][j]
                perim += 1

            #---if you hit the boarder and you're on a 1, increment perim
            if j == len(grid[i]) - 1 and cur_bit_val == 1:
                perim += 1

    #---count bit-flips, column by column
    for j in range(len(grid[0])):
        cur_bit_val = 0
        for i in range(len(grid)):
            if grid[i][j] != cur_bit_val:
                cur_bit_val = grid[i][j]
                perim += 1
            
            #---if you hit the boarder and you're on a 1, increment perim
            if i == len(grid) - 1 and cur_bit_val == 1:
                perim +=1
    
    return perim

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

g = [[0,1,0,0,0],
     [1,1,1,1,1],
     [0,1,0,0,0],
     [1,1,0,0,0]]

print(islandPerimeter(g))