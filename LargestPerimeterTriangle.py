import math

#  LeetCode: 976. Largest Perimeter Triangle

def largestPerimeter(a:[int]) -> int:
    
    a.sort()
    print(a)

    while True:
        h = a.pop()
        la = len(a)
        if la >= 2:
            print(h, a[la-1], a[la-2], math.hypot(a[la-1], a[la-2]))
            if math.hypot(a[la-1], a[la-2]) == h:
                return sum([a[la-1], a[la-2], h])
        else:
            break
    
    return 0
        
    return a

a = [3,2,3,4]
a = [3,6,2,3]
#a = [2,1,2]
print(largestPerimeter(a))
