

# LeetCode: 892. Surface Area of 3D Shapes

def surfaceArea(grid: [[int]]):

    r = []
    N = len(grid)
    bottom = 0
    top = 0
    corner = 0
    edge = 0
    redge = 0
    cedge = 0

    for i in range(len(grid)):
        print(grid[i])
        for j in range(len(grid[i])):
            if grid[i][j] > 0:
                bottom += 1

            if i == 0 or i == N - 1:
                if j == 0 or j == N - 1:
                    corner += grid[i][j]*2
                else:
                    edge += grid[i][j]
            
            if j == 0 or j == N - 1:
                if i > 0 and i < N -1:
                    edge += grid[i][j]

            if j > 0 and j < N:
                redge += abs(grid[i][j] - grid[i][j-1])
            if i > 0 and i < N:
                cedge += abs(grid[i][j] - grid[i-1][j])
    
    #--corner case:
    if N == 1:
        corner *= 2

    top = bottom
    r = [bottom, top, corner, edge, redge, cedge]
    
    return sum(r)

#g = [[1,2,1],[3,4,1],[1,1,2]]
#g = [[2]]
#g = [[1,2],[3,4]]
#g = [[1,0],[0,2]]
g = [[3]]
#g = [[1,1,1],[1,0,1],[1,1,1]]
#g = [[2,2,2],[2,1,2],[2,2,2]]
print(surfaceArea(g))
