# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def bfs(self):

        rlist = []
        q = []
        q.append(self)


        while len(q):
            cur_node = q.pop(0)
            rlist.append(cur_node.val)

            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        
        return rlist
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        return None

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if t1 == None:
            return t2
        if t2 == None:
            return t2
        
        t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1

#------------------------------------------------------------------

t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
(t1.left).left = TreeNode(5)

t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
(t2.left).right = TreeNode(4)
(t2.right).right = TreeNode(7)

print("t1", t1.bfs())
print("t2", t2.bfs())

s = Solution()
tr = s.mergeTrees(t1, t2)
print("tr", tr.bfs())
