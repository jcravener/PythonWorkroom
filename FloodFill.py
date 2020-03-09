

# LeetCode: 733: Flood Fill

def floodFill(image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
    if image[sr][sc] == newColor:
        return image
    
    return helper(image, sr, sc, image[sr][sc], newColor)

def helper(image: [[int]], sr: int, sc: int, oldColor, newColor: int) -> [[int]]:
    if sr < 0 or sr >= len(image):
        return image
    if sc < 0 or sc >= len(image[0]):
        return image
    if image[sr][sc] != oldColor:
        return image
    
    image[sr][sc] = newColor
    
    image = helper(image, sr+1, sc, oldColor, newColor)
    image = helper(image, sr-1, sc, oldColor, newColor)
    image = helper(image, sr, sc+1, oldColor, newColor)
    image = helper(image, sr, sc-1, oldColor, newColor)

    return image

img = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newcolor = 2

for r in img:
    print(r)
print()
for r in floodFill(img, sr, sc, newcolor):
    print(r)