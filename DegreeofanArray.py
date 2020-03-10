

# LeetCode: 697. Degree of an Array

def findShortestSubArray(nums: [int]) -> int:
    d = {}
    l = []
    numsrev = nums[::-1]

    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    
    mxval = max(d, key=lambda k: d[k])
    deg = d[mxval]

    for k, v in d.items():
        if v == deg:
            l.append(len(nums) - numsrev.index(k) - nums.index(k))  #--- this is my on invention :).  It finds the length of the subarray by calulating the distance between the first degree val on the left with the last degree val on the right.
    
    return min(l)

inpt = [1,2,2,3,1,4,2]
inpt = [1, 2, 2, 3, 1]
print(findShortestSubArray(inpt))