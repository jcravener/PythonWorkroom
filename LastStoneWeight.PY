def lastStoneWeight(stones: [int]) -> int:
    if len(stones) == 0:
        return 0
        
    while len(stones) > 1:
        stones.sort()
        x, y = stones[-2:]
        stones = stones[:-2]

        if x != y:
            stones.append(y-x)
    
    if len(stones) == 0:
        return 0
    
    return stones[0]
    

def helper(stns: [int]) -> [int]:
    q = []
    stns.sort()

    if len(stns) >= 2:
        q.append(stns.pop())
        q.append(stns.pop())
    else:
        return stns
    
    if q[0] == q[1]:
        return stns
    elif q[0] >= q[1]:
        stns.append(q[0] - q[1])
    
    return stns

s = [2,7,4,1,8,1]
print(lastStoneWeight(s))