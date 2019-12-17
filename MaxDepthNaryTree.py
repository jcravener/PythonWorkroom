

class node:
    def __init__(self, data=None):
        self.data = data
        self.children = []

def bfs(rt: node):
    q = [rt]
    r = []

    while q:
        cur_node = q.pop(0)

        r.append(cur_node.data)

        if cur_node.children:
            for c in cur_node.children:
                q.append(c)
    return r


# -- this is the Leet Code solution function
#
def maxDepth(rt: node):

    if not rt:
        return 0
    
    q = [rt]
    depth = 0

    while q:
        depth += 1
        child_queue = []

        for n in q:
            if n.children:
                child_queue.extend(n.children)
        
        q = child_queue
    
    return depth

nd1 = node(1)

for i in range(2,6):
    nd1.children.append(node(i))

for n in nd1.children:
    if n.data == 3:
        for i in range(6,8):
            n.children.append(node(i))
    
    if n.data == 4:
        n.children.append(node(8))
    
    if n.data == 5:
        for i in range(9,11):
            n.children.append(node(i))

print(maxDepth(nd1))