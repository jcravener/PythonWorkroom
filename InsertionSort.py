import random


#-- Insertion Sort study

def insertionsort(a:[int]):
    if len(a) == 0:
        return []

    for i in range(1,len(a)):
        key = a[i]
        j = i-1

        while j >=0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

    return a


def insertionsort2(a:[int]):
    if len(a) == 0:
        return a
    
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a


def insertionsort3(a:[int]):
    if len(a) == 0:
        return None
    
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
        
    return a

def insertionsort4(a:[int]):
    if len(a) == 0:
        return None
    
    for i in range(1, len(a)):
        key = a[i] #-- right one: 1
        print("key", key, a)
        j = i-1  #-- left one: 0
        while j >= 0 and a[j] > key: #-- true and 7 > 1
            a[j+1] = a[j]  #-- a[1] = a[0]: 1 = 7
            j -= 1 #-- -1
        a[j+1] = key
        print("key", a[j+1], a)
        print()
    return a

def insertionsort5(a:[int]):
    if len(a) == 1:
        return None
    
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

r = 10
l = []
for _ in range(r):
    l.append(random.randrange(r))

print(l)
print(insertionsort5(l))