

# LeetCode: 697. Degree of an Array

def findShortestSubArray(nums: [int]) -> int:
    d = {}

    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    
    return d

inpt = [1,2,2,3,1,4,2]
print(findShortestSubArray(inpt))