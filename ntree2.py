

class node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = []

class ntree:
    def __init__(self,val=None):
        self.root = node(val)
    
    def add_child(self, val=None):
        cur_node = self.root
        new_node = node(val)

        cur_node.children.append(new_node)
    
class walk:
    def __init__(self):
        return
    def traverse(self, rt: node):

        r = []
        q = [rt]

        while q:
            cur_node = q.pop()

            if cur_node:
                r.append(cur_node.val)

                for c in cur_node.children:
                    q.append(c)
        
        return r[::-1]

    def rtraverse(self,rt: node):
        if not rt:
            return []
        
        r = [rt.val]

        def helper(rt):

            for c in rt.children:
                r.append(c.val)
                helper(c)
        
        helper(rt)
        return r
        
t = ntree(10)
t.add_child(14)
t.add_child(15)
t.add_child(16)
w = walk()

print(w.traverse(t.root))
print(w.rtraverse(t.root))