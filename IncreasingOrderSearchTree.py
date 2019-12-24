class node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: node):
        l = self.inorder_traversal(root)

        cur_node = node(l[0])
        rt = cur_node

        for v in l[1:]:
            cur_node.right = node(v)
            cur_node = cur_node.right
        
        return rt
    
    def inorder_traversal(self, root: node):
        l = []

        if root:
            l = self.inorder_traversal(root.left)
            l.append(root.val)
            l = l + self.inorder_traversal(root.right)
        
        return l

    def stack_traversal(self, root: node):
        s = []
        r = []
        s.append(root)


r = node(5)
r.left = node(3)
r.right = node(6)

(r.left).left = node(2)
(r.left).right = node(4)

(r.right).right = node(8)

s = Solution()
print(s.inorder_traversal(r))
rr = s.increasingBST(r)

l = []
cur_node = rr
l.append(cur_node.val)
while cur_node.right != None:
    cur_node = cur_node.right
    l.append(cur_node.val)
print(l)
