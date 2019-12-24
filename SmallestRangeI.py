

def smallestRangeI(A: [int], K: int):
    
    d = (max(A)-K) - (min(A)+K)

    if d < 0:
        d = 0

    return d

#A = [1]
A = [1,3,6]
#A = [0,10]
K = 2

print(smallestRangeI(A, K))