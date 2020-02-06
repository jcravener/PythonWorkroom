import random

#--- Linked list node class
#
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def addLinkedListData(l1:node,l2:node):
    
    if l1 == None:  #--- error checking
        return None
    if l2 == None:
        return None
    
    a1 = []
    a2 = []
    alrg = []

    r = 0
    c = 0

    l3 = None
    cur = l3

    while l1:  #--- storing linked list data in arrays
        a1.append(l1.data)
        l1 = l1.next
    while l2:
        a2.append(l2.data)
        l2 = l2.next
    
    while len(a1) > 0 and len(a2) > 0:  #-- adding data and building return list
        r = a1.pop() + a2.pop() + c

        if r >= 10:  #--- handling carry
            r = r%10
            c = 1
        else:
            c = 0

        l3 = node(r)
        l3.next = cur
        cur = l3
    
    alrg += a1  #--- storing extra data in case one list is longer than the other
    alrg += a2

    while len(alrg) > 0:  #--- adding any extra data to sum
        r = alrg.pop() + c

        if r >= 10:
            r = r%10
            c = 1
        else:
            c = 0

        l3 = node(r)
        l3.next = cur
        cur = l3
    
    if c:  #--- handling case where there's a left over carry
        l3 = node(c)
        l3.next = cur
        cur = l3

    return l3

#--- util functions for 
#    building and displaying
#    linked lists

def buildRandList(r:int):
    mx = 9
    ll = node(random.randrange(mx))
    h = ll
    for _ in range(r-1):
        ll.next = node(random.randrange(mx))
        ll = ll.next
    return h

def listLinkedList(n:node):
    if not n:
        return None
    l = []
    while n:
        l.append(n.data)
        n = n.next
    return l

#--- build and display intput linked lists  
#
l1 = buildRandList(8)
l2 = buildRandList(9)
a1 = listLinkedList(l1)
a2 = listLinkedList(l2)
print("  ", a1)
print(a2)

#--- get sum of list data for validation
#
s1 = ''.join(map(str,a1))
s2 = ''.join(map(str,a2))
print(s1, "+", s2, "=", int(s1) + int(s2))

#--- run solution
#
print(listLinkedList(addLinkedListData(l1,l2)))

