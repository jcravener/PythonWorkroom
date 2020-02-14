
# LeetCode: 888. Fair Candy Swap

def fairCandySwap(A:[int], B:[int]) -> [int]:
    asum = sum(A)
    bsum = sum(B)

    #sum(A) - x + y = sum(B) - y + x
    #2*y = sum(B) - sum(A) + 2*x
    #y = (sum(B) - sum(A))//2 + x

    for x in A:
        if (((bsum - asum)/2) + x) in B:
            return [x,(((bsum - asum)//2) + x)]
    return None

    

a = [1,1]
b = [2,2]
a = [1,2,5]
b = [2,4]
#a = [1,2]
#b = [2,3]
print(fairCandySwap(a,b))