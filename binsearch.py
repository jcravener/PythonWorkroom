


def binsearch(a: [int], v: int):
    if len(a) == 0:
        return -1
    
    start = 0
    end = len(a) - 1
    mid = (start + end) // 2

    while start != end:

        if v < a[mid]:
            end = mid
        elif v > a[mid]:
            start = mid
        else:
            return mid, a[mid]        

        mid = (start + end) // 2
    
    return v, -1

m = 4
a = [i for i in range(0,m,2)]
v = 56

for v in range(0,m,2):
    print(binsearch(a,v))