
import random

#--- merge sort




def mergeSort(a: [int]):
    if len(a) == 1:
        return a
    
    mid = len(a)//2

    lft = mergeSort(a[:mid])
    right = mergeSort(a[mid:])
    return merge(lft, right)

def merge(lft:[int],rt:[int]):

    tmp = []
    li, ri = 0, 0

    while li < len(lft) and ri < len(rt):
        if lft[li] < rt[ri]:
            tmp.append(lft[li])
            li += 1
        else:
            tmp.append(rt[ri])
            ri += 1
    
    tmp += lft[li:]
    tmp += rt[ri:]

    return tmp

r = 100
l = []
for _ in range(r): l.append(random.randrange(r))
print(l)
print(mergeSort(l))







