
# LeetCode: 496. Next Greater Element I
# Successfull submition but only faster than 29%
#

def nextGreaterElement(nums1: [int], nums2: [int]) -> [int]:

    idx = None
    l = []
    llen = 0

    for i in nums1:
        idx = nums2.index(i)
        llen +=1

        for j in range(idx+1, len(nums2)):
            if i < nums2[j]:
                l.append(nums2[j])
                break
        
        if len(l) < llen:
            l.append(-1)

    return l

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))
print()

nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1, nums2))

nums1 = [1,3,5,2,4]
nums2 = [5,4,3,2,1]
print(nextGreaterElement(nums1, nums2))

