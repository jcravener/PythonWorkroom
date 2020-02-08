


# LeetCode 1089. Duplicate Zeros 

class Solution:
    def duplicateZeros(self, arr: [int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        alen = len(arr)
        tmp =[0]
        i = 0
        
        while i < alen:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop()
                i += 1
            i += 1
        
        print(arr)

s = Solution()
a = [1,0,2,3,0,4,5,0]
s.duplicateZeros(a)
print(a)