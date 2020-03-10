

# LeetCode 167. Two Sum II - Input array is sorted

# First solution was slow: O(n**2) even though I chopped the list a bit in the beginning.
# Since the input array is sorted, need to look for a way to use some kind of binary
# search technique.
# 
# Actaully discovered that the 2-pointer method (which leverages the input array being
# sorted) brought the runtime up from 6476ms to 60ms! 
#

def twoSum(numbers: [int], target: int) -> [int]:
    n = [i for i in numbers if i <= target]
    if len(n) < len(numbers):
        n.append(numbers[len(n)])

    #-- two pointer method -- not doing any bin search teqnique here though
    a = 0
    b = len(n) - 1

    while a != b:
        if n[a] + n[b] == target:
            return [a+1,b+1]
        elif n[a] + n[b] > target:
            b -= 1
        else:
            a += 1

    return None


#numbers = [2,7,11,15,16,17,22,26,28]
#target = 37
numbers = [-4,-2,-1,0]
target = -1
print(twoSum(numbers, target))