

def binsearch(a:[int], v:int):
    
    if v < a[0] or v > a[len(a)-1]:
        return None
    
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        print(start, mid, end, a[start:mid+1],a[mid:end+1])

        if v < a[mid]:
            end = mid - 1
        elif v > a[mid]:
            start = mid + 1
        else:
            return mid, a[mid]

    return None

def binsrch2(a:[int], v:int):
    if v < a[0] or v > a[len(a)-1]:
        return None
    
    start  = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        
        if v < a[mid]:
            end = mid - 1
        elif v > a[mid]:
            start = mid + 1
        else:
            return v, a[mid:mid+1]
    
    return None

a = [i for i in range(10)]
#print(binsearch(a,9))
print(binsrch2(a,9))
