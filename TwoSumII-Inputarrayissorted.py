

# LeetCode 167. Two Sum II - Input array is sorted

# First solution was slow: O(n**2) even though I chopped the list a bit in the beginning.
# Since the input array is sorted, need to look for a way to use some kind of binary
# search technique.  
#

def twoSum(numbers: [int], target: int) -> [int]:
    n = [i for i in numbers if i <= target]
    if len(n) < len(numbers):
        n.append(numbers[len(n)])

    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i] + n[j] == target:
                return [i+1, j+1]
    
    return None


#numbers = [2,7,11,15,16,17,22,26,28]
#target = 37
numbers = [-4,-2,-1,0]
target = -1
print(twoSum(numbers, target))