# LeetCode: 136 Single Number

def singleNumber(nums:[int]) -> int:

    s = set()

    for n in nums:
        if n not in s:
            s.add(n)
        else:
            s.discard(n)
    return s.pop()

a = [2,2,1]
print(singleNumber(a))
a = [4,1,2,1,2]
print(singleNumber(a))