



def binsearch(a:[],v:int):    
    a.sort()

    if v < a[0] or a[len(a)-1] < v:
        return None

    left = 0
    right = len(a) #-- this is one outide of the boundry
    mid = (left + right) // 2

    while left < right:
        if v < a[mid]:
            right = mid
        elif v > a[mid]:
            left = mid
        else:
            return a[mid]
        
        mid = (left + right) // 2
        print(left, mid, right)

    return None

l = [i for i in range(1137,-1,-1)]

print(binsearch(l, 44))