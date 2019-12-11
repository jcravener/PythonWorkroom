


class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def preorder_traverse(root: node):

    print(root.data)

    if root.left:
        return preorder_traverse(root.left)
    if root.right:
        return preorder_traverse(root.right)

def bfs(root: node):
    q = []
    r = []
    q.append(root)

    while q:
        cur_node = q.pop(0)
        r.append(cur_node.data)

        if cur_node.right:
            q.append(cur_node.right)
        if cur_node.left:
            q.append(cur_node.left)
    
    return r

l = node(8)
r = node(12)

rt = node(10)
rt.left = l
rt.right = r

ll = node(9)
lr = node(6)

l.left  = ll
l.right = lr

preorder_traverse(rt)
print(bfs(rt))
