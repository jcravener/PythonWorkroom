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
print()

class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

def listll(n:node):
    tmp = []
    
    while n != None and len(tmp) < 40:
        tmp.append(n.data)
        n = n.next
    return tmp

def findllnode(n:node, v:int):
   
    while n != None:
        if n.data == v:
            return n
        n = n.next
    return None

def buildll(n:node, r:[int]):
    h = n
    for d in r:
        n.next = node(d)
        n = n.next
    return h

r = 10
n = node(0)
l1 = buildll(n, [i for i in range(1,10)])
print(listll(l1))

(findllnode(l1,9)).next = (findllnode(l1,5))
print()
print(listll(l1))

def findloop(n:node):
    if n.next == None:
        return n
    
    slow = n
    fast = slow.next

    while slow and fast:
        if slow == fast:
            return slow, slow.data
        else:
            slow = slow.next
            fast = fast.next.next
    
    return None

print(findloop(l1))


class treeNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def preDFSrec(rt:treeNode):
    if rt == None:
        return None
    tmp = []
    
    tmp.append(rt.data)
    if rt.left:
        tmp += preDFSrec(rt.left)
    if rt.right:        
        tmp += preDFSrec(rt.right)
    
    return tmp

def postDFSrec(rt:treeNode):
    if rt == None:
        return None
    tmp = []
    
    if rt.left:
        tmp += preDFSrec(rt.left)
    if rt.right:        
        tmp += preDFSrec(rt.right)
    tmp.append(rt.data)
    
    return tmp

def inDFSrec(rt:treeNode):
    if rt == None:
        return None
    tmp = []
    

    if rt.left:
        tmp = preDFSrec(rt.left)
    tmp.append(rt.data)
    if rt.right:        
        tmp += preDFSrec(rt.right)

    return tmp

def BFSit(rt:treeNode):
    q = [rt]
    tmp = []

    while q:
        cur = q.pop(0)
        tmp.append(cur.data)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return tmp

def BFSlevels(rt:treeNode):
    q = [rt]
    l = []

    while q:
        lq = []
        tmp = []
        
        for n in q:
            tmp.append(n.data)
            if n.left:
                lq.append(n.left)
            if n.right:
                lq.append(n.right)
        
        l.append(tmp)
        tmp = []
        q = lq
        lq = []
    
    return l
        


rt = treeNode(19)
rt.left = treeNode(8)
rt.left.left = treeNode(6)
rt.left.right = treeNode(14)
rt.right = treeNode(30)
rt.right.left = treeNode(27)
rt.right.right = treeNode(42)

print(preDFSrec(rt))
print(postDFSrec(rt))
print(inDFSrec(rt))
print(BFSit(rt))
print(BFSlevels(rt))







