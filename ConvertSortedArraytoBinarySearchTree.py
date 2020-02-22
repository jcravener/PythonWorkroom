

# LeetCode: 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder_DFS(rt: TreeNode):
    if rt == None:
        return None
    
    l = []

    if rt.left:
        l = inorder_DFS(rt.left)
    l.append(rt.val)
    if rt.right:
        l += inorder_DFS(rt.right)
    
    return l

def BFS(rt: TreeNode):
    l = []
    q = [rt]

    while len(q) != 0:
        cur = q.pop(0)
        l.append(cur.val)
        if cur.left: q.append(cur.left)
        if cur.right: q.append(cur.right)
    
    return l

def sortedArrayToBST(nums: [int]) -> TreeNode:

    if len(nums) == 0:
        return None
    else:
        mid = len(nums)//2
        rt = TreeNode(nums[mid])

        rt.left = sortedArrayToBST(nums[:mid])
        rt.right = sortedArrayToBST(nums[mid+1:])
    
    return rt

a = [-10,-3,0,5,9]
print(inorder_DFS(sortedArrayToBST(a)))
print(BFS(sortedArrayToBST(a)))

