


class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def preorder_traverse(root: node):
    l = []
    
    if root:
        l.append(root.data)
        l = l + preorder_traverse(root.left)
        l = l + preorder_traverse(root.right)
    
    return l

def postorder_traverse(root: node):
    l = []
    
    if root:
        l = postorder_traverse(root.left)
        l = l + postorder_traverse(root.right)
        l.append(root.data)

    return l

def inorder_traverse(root: node):
    l = []
    
    if root:
        l = inorder_traverse(root.left)
        l.append(root.data)
        l = l + inorder_traverse(root.right)

    return l

def increasingtree(root: node):

    l = inorder_traverse(root)
    
    cur_node = node(l[0])
    rt = cur_node
    
    for d in l[1:]:
        cur_node.right = node(d)
        cur_node = cur_node.right
    
    return rt


def inorder_display(root: node):

    if root:
        inorder_display(root.left)
        print(root.data)
        inorder_display(root.right)
    return None

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


rt = node(5)
rt.left = node(3)
rt.right = node(6)

(rt.left).left = node(2)
(rt.left).right = node(4)
((rt.left).left).left = node(1)

(rt.right).right = node(8)
((rt.right).right).left = node(7)
((rt.right).right).right = node(9)

print(preorder_traverse(rt))
print(postorder_traverse(rt))
print(inorder_traverse(rt))

newrt = increasingtree(rt)

print(inorder_traverse(newrt))

#print(bfs(rt))
