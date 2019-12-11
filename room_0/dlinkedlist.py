

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

class dlnkdlst:
    def __init__(self):
        self.head = node()
        self.tail = self.head
        self.count = 0
    
    def append(self,data=None):
        tail = self.tail
        new_node = node(data)

        tail.next = new_node
        new_node.previous = tail

        self.tail = new_node
        self.count +=1

    def fw_display(self):
        cur_node = self.head
        r = []

        while cur_node.next != None:
            cur_node = cur_node.next
            r.append(cur_node.data)
        
        return r
    
    def rv_display(self):
        cur_node = self.tail
        r = []

        while cur_node.previous != None:
            r.append(cur_node.data)
            cur_node = cur_node.previous
        
        return r
    
    def find_val(self,val):
        cur_node = self.head
        cur_idx = 0

        while cur_node.next != None:
            cur_node = cur_node.next

            if cur_node.data == val:
                return cur_idx, cur_node.data
            cur_idx += 1
    
    def remove(self,index):
        
        if 0 > index >= self.count:
            return None
        
        if index > self.count//2:
            cur_node = self.tail
            cur_idx = self.count - 1

            while cur_idx != index:
                cur_node = cur_node.previous
                cur_idx -= 1
        else:
            cur_node = (self.head).next
            cur_idx = 0

            while cur_idx != index:
                cur_node = cur_node.next
                cur_idx += 1
        
        next_node = cur_node.next
        prev_node = cur_node.previous

        prev_node.next = next_node
        next_node.previous = prev_node

        self.count -= 1

            




dll = dlnkdlst()
for i in range(10):
    dll.append(i)

print(dll.fw_display())
print(dll.rv_display())

print(dll.find_val(9))
dll.remove(7)
print(dll.fw_display())
print(dll.rv_display())
