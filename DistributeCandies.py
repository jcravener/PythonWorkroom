

# LeetCode: 575. Distribute Candies

def distributeCandies(candies: [int]) -> int:
    if len(candies) == 0:
        return []
    
    mx = len(candies) // 2
    d = {}

    for e in candies:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

    return min(mx, len(d))

def distributeCandiesSt(candies: [int]) -> int:
    ln = len(candies)

    if ln == 0:
        return []
    
    st = set(candies)

    return min(len(st), ln//2)


candies = [1,1,2,2,3,3]
print(distributeCandies(candies))
print(distributeCandiesSt(candies))
candies = [1,1,2,3]
print(distributeCandies(candies))
print(distributeCandiesSt(candies))
