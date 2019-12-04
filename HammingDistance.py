


def hammingDistance(x: int, y: int):

    xs = bin(x)
    ys = bin(y)

    xs = xs.split('b')[1]
    ys = ys.split('b')[1]

    if len(xs) > len(ys):
        ys = ys.zfill(len(xs))
    elif len(xs) < len(ys):
        xs = xs.zfill(len(ys))
    
    result = 0

    for i in range(len(xs)):
        xi = int(xs[i])
        yi = int(ys[i])

        if xi + yi == 1:
            result += 1
    
    return result

def hammingDistanceOptimized(x: int, y: int):

    s = bin(x^y)
    result = 0

    for c in s:
        if c == '1': result += 1
    
    return result




















#-------------------------------------------------------------------------------------------------

x = 1
y = 44

print(hammingDistance(x,y))

print(hammingDistanceOptimized(x,y))