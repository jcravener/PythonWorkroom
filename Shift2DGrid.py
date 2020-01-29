

# LeetCode: 1260. Shift 2D Grid

def shiftGrid(grid: [[int]], k: int) -> [[int]]:
    ilen = len(grid)
    jlen = len(grid[0])
    
    l = []
    for i in grid:
        l += i
    lenl = len(l)
    
    if k == lenl:
        return grid
    elif k < lenl:
        # shift by k
        ll = l[:k] + l[k:]
    #else:
        # shift by k%lenl

    return l, ll

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(shiftGrid(grid,k))

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
print(shiftGrid(grid,k))
