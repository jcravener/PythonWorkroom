

# LeetCode: 1013. Partition Array Into Three Parts With Equal Sum

def canThreePartsEqualSum(A: [int]) -> bool: 

    prt = sum(A)//3
    sm = 0
    ct = 0

    for e in A:
        sm += e
        if sm == prt:
            ct += 1
            sm = 0
    if ct == 3:
        return True
    else:
        return False


a = [0,2,1,-6,6,-7,9,1,2,0,1]
b = [0,2,1,-6,6,7,9,-1,2,0,1]
c = [3,3,6,5,-2,2,5,1,-9,4]
d = [a,b,c]

for e in d:    
    print(canThreePartsEqualSum(e))



