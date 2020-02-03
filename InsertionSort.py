import random


#-- Insertion Sort study

def insertionsort(a:[int]):
    if len(a) == 0:
        return []

    for i in range(1,len(a)):
        cur = a[i]
        j = i - 1
        while j >= 0:
            if a[j] < cur:
                a[j], cur = cur, a[j]

            j -= 1
        i += 1

    
    return a

r = 10
l = []
for _ in range(r):
    l.append(random.randrange(r))

print(l)
print(insertionsort(l))