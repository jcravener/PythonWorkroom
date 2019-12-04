
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

#------------------------------------------------------------------------

ll = linekedlist()
for i in range(10): ll.append(i)
ll.display()

print()
print(ll.findval(4))

print()
print(ll.getindex(4))

print()
print(ll.size())

print()
ll.remove(4)
ll.display()
print(ll.size())

print()
ll.insert(4,99)
ll.display()
print(ll.size())
