

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)

class linkedlist:
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        current = self.head

        while current.next != None:
            current = current.next
        
        current.next = new_node

    def display(self):
        a = []
        current = self.head
        while current.next != None:
            current = current.next
            a.append(current.data)
        
        print(a)

    def length(self):
        l = 0
        current = self.head
        while current.next != None:
            l += 1
            current = current.next
        
        return l

    def get(self, index):
        
        if index >= self.length():
            return None
        
        current = self.head
        cur_idx = 0
        while current.next != None:
            current = current.next

            if cur_idx == index:
                return current.data
            cur_idx += 1

    def remove(self, index):

        if index >= self.length():
            return None
        
        current = self.head
        cur_idx = 0

        while current.next != None:
            last = current
            current = current.next
            if cur_idx == index:
                last.next = current.next
                return
            cur_idx += 1
    
    def gethead(self):
        return self.head.data

    def insert(self, index, data):

        if index >= self.length():
            self.append(data)

        new_node = node(data)
        current = self.head
        cur_idx = 0

        while current.next != None:
            last = current
            current = current.next

            if cur_idx == index:
                last.next = new_node
                new_node.next = current
                return
            cur_idx += 1

ll = linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()

ll.remove(1)
ll.display()

ll.insert(0,9)
ll.display()

ll.insert(2,11)
ll.display()
