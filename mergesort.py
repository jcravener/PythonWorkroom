
import random

# Merge Sort Study

def mergesort(a: [int], left:int, right:int):
    if left == right:
        return a
    
    #-- split array into 2 and pass back to mergesort

    mid = (left + right) // 2

    print(l[left:mid], l[mid:right])
    return merge(l[left:mid], l[mid:right])

def merge(l:[], r:[]):
    if len(l) == 0:
        return r
    if len(r) == 0:
        return l
    tmp = []

    if len(l) < len(r):
        for i in range(len(l)):
            if l[i] < r[i]:
                tmp.append(l[i])
                tmp.append(r[i])
            else:
                tmp.append(r[i])
                tmp.append(l[i])
        tmp += r[len(l):]  
    else:
        for i in range(len(r)):
            if l[i] < r[i]:
                tmp.append(l[i])
                tmp.append(r[i])
            else:
                tmp.append(r[i])
                tmp.append(l[i])
    
    if len(l) > len(r):
        tmp += l[len(r):]

    return tmp






    





r = 19
l = []
for _ in range(r):
    l.append(random.randrange(r)-1)

print(l)
print(mergesort(l, 0, len(l)) )