
def relativeSortArray(arr1: [], arr2: []):

    r = []
    n = []

    for i in arr1:
        if i not in arr2:
            n.append(i)
    n.sort()
    
    for i in arr2:
        for j in range(arr1.count(i)):
            r.append(i)
    
    r.extend(n)

    return r

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(relativeSortArray(arr1, arr2))