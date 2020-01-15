
class node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class linekedlist():
    def __init__(self):
        self.head = node()
        self.length = 0
    
    def append(self,data):
        new_node = node(data)
        cur_node = self.head

        while cur_node.next != None:
            cur_node = cur_node.next
        
        cur_node.next = new_node
        new_node.prev = cur_node
        self.length += 1
    
    def display(self):
        cur_node = self.head
        rlist = []

        while cur_node.next != None:
            cur_node = cur_node.next
            rlist.append(cur_node.data)

        print(rlist)
    
    def findval(self,val):
        cur_node = self.head
        cur_idx = 0

        while cur_node.next != None:
            cur_node = cur_node.next

            if cur_node.data == val:
                return cur_idx
            cur_idx += 1
        
    def getindex(self,idx):

        cur_node = self.head
        rdict = {}
        cur_idx = 0

        while cur_node.next != None:
            cur_node = cur_node.next

            if cur_idx == idx:
                
                rdict = {'prev_val': cur_node.prev.data, 'idx_val': cur_node.data, 'next_val': cur_node.next.data}
                
                return rdict
            
            cur_idx += 1
        
        return None
    
    def size(self):
        return self.length

    def remove(self, index):
        cur_node = self.head
        cur_idx = 0

        while cur_node.next != None:
            cur_node = cur_node.next
            prv_node = cur_node.prev
            nxt_node = cur_node.next

            if cur_idx == index:
                prv_node.next = nxt_node
                nxt_node.prev = prv_node
                self.length -= 1
                return
            
            cur_idx += 1

        return None

    def insert(self,index,data):
        new_node = node(data)
        cur_node = self.head
        cur_idx = 0

        while cur_node.next != None:
            cur_node = cur_node.next
            prv_node = cur_node.prev

            if cur_idx == index:
                prv_node.next = new_node
                new_node.prev = prv_node
                new_node.next = cur_node
                cur_node.prev = new_node
                self.length += 1
                return
            
            cur_idx += 1
        
        return None
    
    def getnode(self, index):
        cur_node = self.head
        cur_idx = 0

        while cur_node.next != 1:
            cur_node = cur_node.next

            if cur_idx == index:
                return cur_node
            
            cur_idx += 1
        
        return None


def llMergeCheck(l1: node, l2: node):

    s = set()

    while l1.next:
        s.add(l1)
        l1 = l1.next
    
    while l2.next:
        if l2 in s:
            return l2.data
        else:
            s.add(l2)
        l2 = l2.next
    
    return None

def llLoopCheck(l1: node):

    if l1 == None or l1.next == None:
        return None
    
    slw = l1
    fst = l1.next

    while slw and fst.next:  #--- need to check fst.next otherwise lists without loop errors

        if slw == fst:
            return slw.data, slw.next.data
        
        slw = slw.next
        fst = fst.next.next
    
    return None

def llLoopCheckWithSet(l1: node):
    
    if l1 == None or l1.next == None:
        return None
    
    s = set()
    prv = l1

    while l1:
        if l1 in s:
            return prv.data, l1.data
        else:
            s.add(l1)
        
        prv = l1
        l1 = l1.next
    
    return None

#------------------------------------------------------------------------

l1 = linekedlist()
for i in range(10): l1.append(i)
l1.display()

l2 = linekedlist()
for i in range(20,26): l2.append(i)
l2.display()
print()

n1 = l1.getnode(0)
n2 = l2.getnode(0)
print(llMergeCheck(n1, n2))

(l2.getnode(4)).next = (l1.getnode(5))
print()
l1.display()
l2.display()
print()

n1 = l1.getnode(0)
n2 = l2.getnode(0)
print(llMergeCheck(n1, n2))
print(llMergeCheck(n2, n1))
print()

l3 = linekedlist()
for i in range(10,20): l3.append(i)
l3.display()
(l3.getnode(9)).next = (l3.getnode(5))

n3 = l3.getnode(0)

l = []
for _ in range(20):
    l.append(n3.data)
    n3 = n3.next

print(l)
n3 = l3.getnode(0)
print(llLoopCheck(n3))
print()
print(llLoopCheckWithSet(n3))

n4 = node(0)
n4.next = n4
print(llLoopCheck(n4))
print(llLoopCheckWithSet(n4))

print()
print(llLoopCheckWithSet(l1.getnode(0)))
print(llLoopCheck(l1.getnode(0)))