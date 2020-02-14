
# LeetCode: 888. Fair Candy Swap

def fairCandySwap(A:[int], B:[int]) -> [int]:
    asum = sum(A)
    bsum = sum(B)
    delt = abs(asum - bsum)//2
    
    if asum > bsum:
        lrg = A
        sml = B
    else:
        lrg = B
        sml = A
    
    for a in lrg:
        for b in sml:
            if a - b == delt:
                if asum > bsum:
                    return [a,b]
                else:
                    return [b,a]
    return None

a = [1,1]
b = [2,2]
#a = [1,2,5]
#b = [2,4]
#a = [1,2]
#b = [2,3]
print(fairCandySwap(a,b))