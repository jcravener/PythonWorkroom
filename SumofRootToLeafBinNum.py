class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def btreepath(r: TreeNode):

    if r == None:
        return None

    s = [[r, ""]]
    base = "0b"
    ct = 0

    while s:
        cur_node, path = s.pop()

        if cur_node.left:
            s.append([cur_node.left, path+str(cur_node.val)])
        if cur_node.right:
            s.append([cur_node.right, path+str(cur_node.val)])
        
        if cur_node.left == None and cur_node.right == None:
            path += str(cur_node.val)
            ct += int(base + path, 2)
    
    return ct
    
r = TreeNode(1)
r.left = TreeNode(0)
r.right = TreeNode(1)
r.left.left = TreeNode(0)
r.left.right = TreeNode(1)
r.right.left = TreeNode(0)
r.right.right = TreeNode(1)

print(btreepath(r))


