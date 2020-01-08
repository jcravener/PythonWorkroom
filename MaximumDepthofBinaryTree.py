class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root: TreeNode):

    if root == None:
        return root
    
    s = [[root, 1]]
    mxd = set()

    while s:
        cur_node, depth = s.pop()

        if cur_node.left:
            s.append([cur_node.left, depth+1])
        if cur_node.right:
            s.append([cur_node.right, depth+1])        
        
        if cur_node.left == None and cur_node.right == None:
            mxd.add(depth)

    return max(mxd)


def inorderdfs(root: TreeNode):
    if root == None:
        return None

    l = []

    if root.left:
        l = inorderdfs(root.left)
    l.append(root.val)
    if root.right:
        l = l + inorderdfs(root.right)
    
    return l

r = TreeNode(3)
r.left = TreeNode(9)
r.right = TreeNode(20)
r.right.left = TreeNode(15)
r.right.right = TreeNode(7)

#print(inorderdfs(r))
print(maxDepth(r))


