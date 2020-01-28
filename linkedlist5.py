
# Link list study

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def listll(n: Node):
    l = []
    while n != None:
        l.append(n.val)
        n = n.next
    return l

def buildll(n: Node, start: int, stop: int):
    for i in range(start, stop):
        n.next = Node(i)
        n = n.next
def getnode(n: Node, v):
    while n != None:
        if n.val == v:
            return n
        n = n.next
    return None

def findmerge(n1: Node, n2: Node):
    st = set()

    while n1 or n2:
        if n1:
            if n1 in st:
                return 'n1', n1.val
            else:
                st.add(n1)
            n1 = n1.next
        if n2:
            if n2 in st:
                return 'n2', n2.val
            else:
                st.add(n2)
            n2 = n2.next
    return None, None 

def findmergeStk(n1: Node, n2: Node):
    stk1 = []
    stk2 = []
    
    while n1:
        stk1.append(n1)
        n1 = n1.next
    while n2:
        stk2.append(n2)
        n2 = n2.next

    if stk1[len(stk1)-1] != stk2[len(stk2)-1]:  #-- no merge at all
        return None, None

    if len(stk1) > len(stk2):
        prev = stk2[len(stk2)-1]
        while len(stk2):
            cur1, cur2 = stk1.pop(), stk2.pop()
            if cur1 != cur2:
                return 'n2', prev.val
            else:
                prev = cur1
    else:
        prev = stk1[len(stk1)-1]
        while len(stk1):
            cur1, cur2 = stk1.pop(), stk2.pop()
            if cur1 != cur2:
                return 'n1', prev.val
            else:
                prev = cur1
    
    return None


l1 = Node(0)
buildll(l1,1,10)
l2 = Node(3)
buildll(l2,4,6)
print(listll(l1))
print(listll(l2))
print(findmerge(l1, l2))

(getnode(l2,5)).next = getnode(l1,6)
print(listll(l1))
print(listll(l2))

print(findmerge(l1, l2))
print()
print(findmergeStk(l1, l2))
print()

la = Node(4)
la.next = Node(1)
lb = Node(5)
lb.next = Node(0)
lb.next.next = Node(1)
lc = Node(8)
lc.next = Node(4)
lc.next.next = Node(5)

print(listll(la))
print(listll(lb))
print(listll(lc))
print(findmerge(la, lb))
print(findmergeStk(la,lb))
print()
(getnode(la, 1)).next = lc
(getnode(lb, 1)).next = lc
print(listll(la))
print(listll(lb))
print(findmerge(la, lb))
print(findmergeStk(la, lb))

