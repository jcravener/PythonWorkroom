
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

def insertBstNode(rt:TreeNode, v: int) -> TreeNode:
    if rt == None:
        return None
    nnode = TreeNode(v)
    
    if v < rt.val:
        if rt.left:
            insertBstNode(rt.left, v)
        else:
            rt.left = nnode
    elif v> rt.val:
        if rt.right:
            insertBstNode(rt.right, v)
        else:
            rt.right = nnode

def midlist(a:[int]) -> int:
    return len(a)//2

def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
    return None

h = TreeNode(1)
h.left = TreeNode(0)
h.right = TreeNode(2)

a = [i for i in inorderDfsTravers(h) if i >= 1 and i <=  2]
print(a)

h = TreeNode(3)
h.left = TreeNode(0)
h.right = TreeNode(4)
(h.left).right = TreeNode(2)
((h.left).right).left = TreeNode(1)
a = [i for i in inorderDfsTravers(h) if i >= 1 and i <=  3]
print(a)

