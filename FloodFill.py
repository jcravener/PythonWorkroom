

# LeetCode: 733: Flood Fill

def floodFill(image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
    if image[sr][sc] == newColor:
        return image
        
    def helper(image: [[int]], sr: int, sc: int, oldColor: int, newColor: int):
        if (0 > sr >= len(image)) or (0 > sc >= len(image[0])):  #---
            return
        print(sr, sc)
        image[sr][sc] = newColor

        helper(image, sr+1, sc, oldColor, newColor)  
        helper(image, sr-1, sc, oldColor, newColor)  
        helper(image, sr, sc+1, oldColor, newColor)  
        helper(image, sr, sc-1, oldColor, newColor)
    
    helper(image, sr, sc, image[sr][sc], newColor)
    return image


img = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newcolor = 2

for r in floodFill(img, sr, sc, newcolor):
    print(r)
    