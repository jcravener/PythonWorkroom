

# LeetCode: 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findTarget(root: TreeNode, k: int) -> bool:
    return None

def inorderDFS(nd: TreeNode):
    if nd == None:
        return None
    l = []

    if nd.left:
        l = inorderDFS(nd.left)
    l.append(nd.val)
    if nd.right:
        l += inorderDFS(nd.right)

    return l

def BFS(nd: TreeNode):

    q = [nd]
    l = []

    while q:
        cur = q.pop(0)
        l.append(cur.val)

        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    
    return l


rt = TreeNode(5)
rt.left = TreeNode(3)
rt.left.left = TreeNode(2)
rt.left.right = TreeNode(4)
rt.right = TreeNode(6)
rt.right.right = TreeNode(7)

print(inorderDFS(rt))
print(BFS(rt))