#
# LeetCode: 226. Invert Binary Tree
# After a bit of thinking, solved it with no research
# and used itereative DFS approach.
#
# After some reseach, added a recursive approach.
# This used much less code.
#


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    s = [root]
    v = []
    
    while s:
        cur_node = s.pop()

        if cur_node not in v:
            v.append(cur_node)

            if cur_node.left:
                s.append(cur_node.left)
            if cur_node.right:
                s.append(cur_node.right)

            cur_node.left, cur_node.right = cur_node.right, cur_node.left            
    
    return root

def invertTreeRec(root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = invertTreeRec(root.right), invertTreeRec(root.left)
    return root

def BFSdepth(root: TreeNode):
    if not root:
        return None
    
    q = [root]
    l = []

    while q:
        dq = []
        l.append([i.val for i in q])

        for n in q:
            if n.left:
                dq.append(n.left)
            if n.right:
                dq.append(n.right)

        q = dq
    
    return l



r = TreeNode(4)
r.left = TreeNode(2)
r.right = TreeNode(7)

r.left.left = TreeNode(1)
r.left.right = TreeNode(3)

r.right.left = TreeNode(6)
r.right.right = TreeNode(9)

print(BFSdepth(r))
print(BFSdepth(invertTreeRec(r)))
