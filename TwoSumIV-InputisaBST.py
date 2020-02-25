

# LeetCode: 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findTarget(root: TreeNode, k: int) -> bool:

    l = inorderDFS(root)  #  create a sorted array with inorder DFS

    #  check if the sum of the last 2 elements are < target first.
    #  if they not, the remaining combination of all others cannot be.
    if sum(l[len(l)-2:]) < k:
        return False
    
    li = 0
    ri = len(l) - 1
    
    while li != ri:
        if l[li] + l[ri] < k:
            li += 1
        elif l[li] + l[ri] > k:
            ri -= 1
        else:
            return l[li], l[ri], True

    return False


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
print(findTarget(rt,5))