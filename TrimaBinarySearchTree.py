
# LeetCode: 669. Trim a Binary Search Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderDfsTravers(rt:TreeNode) -> TreeNode:

    if rt == None:
        return None
    
    l = []

    if rt.left:
        l = inorderDfsTravers(rt.left)
    l.append(rt.val)
    if rt.right:
        l += inorderDfsTravers(rt.right)
    
    return l

def BSFtraversal(rt:TreeNode):
    if not rt:
        return None
    
    q = [rt]
    l = []

    while q:
        cur_node = q.pop(0)
        l.append(cur_node.val)
        
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    
    return l
        
def insertBstNode(rt:TreeNode, v: int) -> TreeNode:
    if rt == None:
        return None
    nnode = TreeNode(v)
    
    if v < rt.val:
        if rt.left:
            insertBstNode(rt.left, v)
        else:
            rt.left = nnode
    elif v > rt.val:
        if rt.right:
            insertBstNode(rt.right, v)
        else:
            rt.right = nnode

def BSFdepth(rt:TreeNode):
    if not rt:
        return None
    
    q = [rt]
    depth = 0
    da = []

    while q:
        depth += 1
        dq = []

        for n in q:
            if n.left:
                dq.append(n.left)
            if n.right:
                dq.append(n.right)
        
        da.append([i.val for i in dq])
        q = dq
    
    return depth, da

def midlist(a:[int]) -> int:
    return len(a)//2

def trimBST(root: TreeNode, L: int, R: int) -> TreeNode:
    if not root:
        return None
    
    a =  [i for i in BSFtraversal(root) if i >= L and i <= R]
    r = TreeNode(a[0])

    for v in a[1:]:
        insertBstNode(r, v)

    return r

h = TreeNode(1)
h.left = TreeNode(0)
h.right = TreeNode(2)
print(BSFtraversal(trimBST(h, 1, 2)))

h = TreeNode(3)
h.left = TreeNode(0)
h.right = TreeNode(4)
(h.left).right = TreeNode(2)
((h.left).right).left = TreeNode(1)
print(BSFtraversal(trimBST(h, 1, 3)))
