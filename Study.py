import random

# Differnet Functions for Study

class Sort:
    def __init__(self):
        self

    def randomList(self, r:int):
        return [random.randrange(r) for _ in range(r)]

    def quickSort(self, a:[int]):
        if len(a) <= 1:
            return a
        
        pivot = random.choice(a)

        lft = [i for i in a if i < pivot]
        eq = [i for i in a if i == pivot]
        rt = [i for i in a if i > pivot]
        
        return self.quickSort(lft) + eq + self.quickSort(rt)
    
    def mergeSort(self, a:[int]):
        if len(a) == 1:
            return a
        
        mid = len(a)//2
        lft = self.mergeSort(a[:mid])
        rt = self.mergeSort(a[mid:])
        
        return self.__merge(lft, rt)
    
    def __merge(self, l:[int], r:[int]):
        
        tmp = []
        li = 0
        ri = 0

        while li < len(l) and ri < len(r):
            if l[li] < r[ri]:
                tmp.append(l[li])
                li += 1
            else:
                tmp.append(r[ri])
                ri += 1
        tmp += l[li:]
        tmp += r[ri:]

        return tmp
    
    def selectionSort(self, a:[int]):

        for i in range(len(a)):
            min = a[i]
            mini = i
            for j in range(i, len(a)):
                if a[j] < min:
                    min = a[j]
                    mini = j
                j += 1
            a[i], a[mini] = a[mini], a[i]
        
        return a

    def insertionSort(self, a:[int]):

        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            while j >=0 and a[j] > key:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = key
        
        return a

r = 20
srt = Sort()
l = srt.randomList(r)
print(l)
print(srt.quickSort(l))
print()
l = srt.randomList(r)
print(l)
print(srt.mergeSort(l))
print()
l = srt.randomList(r)
print(l)
print(srt.selectionSort(l))
print()
l = srt.randomList(r)
print(l)
print(srt.insertionSort(l))

def perm(s:str):

    tmp = [s]

    for i in range(len(s)):
        for p in perm(s[:i]+s[i+1:]):
            tmp.append(p + s[i])
    
    return tmp

s = 'abc'
print()
print(perm(s))

def palendrone(s:str):
    slst = list(s)

    while len(slst) >= 2:
        if slst.pop(0) != slst.pop():
            return False
    return True

s = 'racecar'
print()
print(palendrone(s))

def revstr(s:str):
    slst = list(s)
    r = ""

    while len(slst):
        r += slst.pop()
    return r

s = "John Cravener"
print(revstr(s))