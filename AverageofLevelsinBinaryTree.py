
# LeetCode: 637. Average of Levels in Binary Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def averageOfLevels(root: TreeNode) -> [float]:
    if not root:
        return None

    q = [root]
    r = []

    while q:
        lev = []
        lval = []

        for n in q:
            lval.append(n.val)
            if n.left:
                lev.append(n.left)
            if n.right:
                lev.append(n.right)
        
        r.append(sum(lval)/len(lval))
        q = lev
    
    return r 

rt = TreeNode(3)
rt.left = TreeNode(9)
#rt.left.left = TreeNode(1)
#rt.left.right = TreeNode(2)
rt.right = TreeNode(20)
rt.right.left = TreeNode(15)
rt.right.right = TreeNode(17)

print(averageOfLevels(rt))
