
import random

# Merge Sort Study

def mergesort(a:[int]):
    if len(a) == 1:
        return a
    
    #start = 0
    #end = len(a) # -- st frist, I was defining end = len(a)-1 and this resulted in a maximum recursion depth exceeded error
    #mid = (start + end)//2
    mid = len(a)//2  #-- both this and the above methods for finding mid works

    lft = mergesort(a[:mid])
    rt = mergesort(a[mid:])
    a = merge(lft,rt)
    return a

def merge(l, r):
    tmp = []
    li, ri = 0, 0

    while li < len(l) and ri < len(r):
        if l[li] < r[ri]:
            tmp.append(l[li])
            li += 1
        else:
            tmp.append(r[ri])
            ri += 1
    
    if len(l[li:]) < len(r[ri:]):
        tmp += r[ri:]
    if len(r[ri:]) < len(l[li:]):
        tmp += l[li:]

    return tmp


#-- this is from leetcode: https://leetcode.com/problems/sort-an-array/discuss/455034/Python-Clean-Merge
#
def sortArray(nums:[int]) -> [int]:
        if len(nums) <= 1: return nums
        mid = len(nums)//2
        left = sortArray(nums[:mid])
        right = sortArray(nums[mid:])
        l,r = 0,0
        sorted_nums = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                sorted_nums.append(left[l])
                l+=1
            else:
                sorted_nums.append(right[r])
                r+=1
        sorted_nums.extend(left[l:])
        sorted_nums.extend(right[r:])
        return sorted_nums


r = 9
l = []
for _ in range(r):
    l.append(random.randrange(r)-1)

mid = (0 + len(l))//2
print(l)
a = l[:mid]
b = l[mid:]
print(a)
print(b)
print(merge(a,b))

#print(sortArray(l))
print(mergesort(l))
