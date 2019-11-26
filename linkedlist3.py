
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

class linked_List:
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        cur_node = self.head
        new_node = node(data)

        while cur_node.next != None:
            cur_node = cur_node.next
        
        cur_node.next = new_node
        new_node.previous = cur_node
    
    def display(self):
        cur_node = self.head
        l = []

        while cur_node.next != None:
            cur_node = cur_node.next
            l.append(cur_node.data)
        
        return l
    
    def insert(self,index,data):
        
        #if index == 0:  #-- can't insert before the head
        #    return None
        
        cur_node = self.head
        new_node = node(data)
        cur_idx = 0

        while cur_node.next != None:
            prev_node = cur_node  #-- save prev node
            cur_node = cur_node.next #-- move on to next node

            if cur_idx == index:  #-- are we on our insert index?
                prev_node.next = new_node #-- point prev node next to new node
                new_node.previous = prev_node #-- point new node prev to prev node
                new_node.next = cur_node #-- point new node next to curr node
                cur_node.prev_node = new_node #---point cur node prev to new node
                return
            cur_idx += 1 #-- update cur_idex
    
    def get_prev_val(self,index):

        if index == 0:  #---can't get prev val of index 0 because it's the head
            return None
        
        cur_node = self.head
        cur_idx = 0

        while cur_node.next != None:
            cur_node = cur_node.next

            if cur_idx == index:
                return cur_node.prev_node.data
            
            cur_idx += 1
    
    def get_next_val(self,index):
        cur_node = self.head
        cur_idex = 0

        while cur_node.next != None:
            cur_node = cur_node.next

            if cur_idex == index:
                return cur_node.next.data
            
            cur_idex += 1

    def remove(self,index):
        
        cur_node = self.head
        cur_idx = 0

        while cur_node.next != None:
            prev_node = cur_node  #-- store the cur node
            cur_node = cur_node.next  #--store the next node
            next_node = cur_node.next

            if cur_idx == index:  #--we're at our index so repoint prev
                prev_node.next = next_node
                next_node.prev = prev_node
                return

            cur_idx += 1
    
    def find(self, data):
        
        cur_node = self.head
        cur_idx = 0
        l = []

        while cur_node.next != None:
            cur_node = cur_node.next

            if data == cur_node.data:
                l.append(cur_idx)
            
            cur_idx += 1

        return l

#--------------------------------------------------------------------------

ll = linked_List()

ll.append(5)
print(ll.display())

ll.insert(0,3)
print(ll.display())

ll.insert(1,4)
print(ll.display())

print(ll.get_prev_val(2))
print(ll.display())

print(ll.get_next_val(1))

ll.remove(0)
print(ll.display())

ll.insert(2,3.5)
print(ll.display())

ll.append(5)
print(ll.display())

print(ll.find(5))

print('-' * 100)