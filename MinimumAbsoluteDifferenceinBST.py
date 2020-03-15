

# LeetCode: 530. Minimum Absolute Difference in BST

#   Solution accepted but only runs 44% faster than online submissions.
#   Runs in O(2N) because it first traverses tree to produce sorted array,
#   then it traverses that array to calulate the min diff. Think I 
#   need to fugure out a way to hafve it run in O(N).  Maybe, calulate
#   the min dif as the tree is being traversed...

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getMinimumDifference(root: TreeNode) -> int:
    l = inorderDFS(root)
    a = []
    
    for i in range(1, len(l)):
        a.append(l[i]-l[i-1])

    return min(a) 

def inorderDFS(rt: TreeNode):
    if not rt:
        return None
    l = []

    if rt.left:
        l.extend(inorderDFS(rt.left))
    l.append(rt.val)
    if rt.right:
        l.extend(inorderDFS(rt.right))
    return l

r = TreeNode(1)
r.right = TreeNode(3)
r.right.left = TreeNode(2)

print(inorderDFS(r))
print(getMinimumDifference(r))