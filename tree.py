


class tree():
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def insert_left(self,data):
        new_node = tree(data)
        
        if self.left:
            new_node.left = self.left
            self.left = new_node
        else:
            self.left = new_node
    
    def insert_right(self,data):
        new_node = tree(data)

        if self.right:
            new_node.right = self.right
            self.right = new_node
        else:
            self.right = new_node
    
    def preorder_dfs(self):
        print(self.data)

        if self.left:
            self.left.preorder_dfs()
        
        if self.right:
            self.right.preorder_dfs()
    
    def inorder_dfs(self):

        if self.left:
            self.left.inorder_dfs()
        
        print(self.data)

        if self.right:
            self.right.inorder_dfs()

    def postorder_dfs(self):

        if self.right:
            self.right.postorder_dfs()
        
        if self.left:
            self.left.postorder_dfs()
        
        #print(self.data)
        return self.data

    def get_postorder_dfs(self):
        r = []
        r.append(self.postorder_dfs())
        return r

    def bfs(self):
        q = []
        q.append(self)

        while len(q) != 0:
            
            cur_node= q.pop(0)
            print(cur_node.data)

            if cur_node.left:
                q.append(cur_node.left)
            
            if cur_node.right:
                q.append(cur_node.right)
    
    def bfs_find(self, data):  # this was the first ver of solution for LeetCode 700
        q = []
        q.append(self)

        while len(q):
            cur_node = q.pop(0)

            if cur_node.data == data:
                return cur_node

            if cur_node.left:
                q.append(cur_node.left)
            
            if cur_node.right:
                q.append(cur_node.right)
    
    def searchBST(self, root, val):  # this was the second, much fater, solution for LeetCoce 700

        if not root:
            return None
        elif root.data == val:
            return root
        elif val < root.data: # take advantage of BST property left child smaller than root
            return self.searchBST(root.left, val)
        else: # take advantage of BST property right child larger than root
            return self.searchBST(root.right, val)



def dfs(r: tree):

    s = [r]
    l = []

    while s:
        cur_node = s.pop()

        if cur_node.left:
            s.append(cur_node.left)

        l.append(cur_node.data)

        if cur_node.right:
            s.append(cur_node.right)
    
    return l

def inorderdfs(r :tree):

    l = []

    if r:
        l = inorderdfs(r.left)
        l.append(r.data)
        l = l + inorderdfs(r.right)
    return l

#------------------------------------------------------------------------

t = tree(5)
t.left = tree(3)
t.right = tree(6)
(t.left).left = tree(2)
(t.left.right) = tree(4)


print()
t.bfs()

print()
(t.bfs_find(2)).bfs()

print()
(t.searchBST(t,2)).bfs()

print()
print(t.get_postorder_dfs())

print()
print(t.postorder_dfs())

print()
print(dfs(t))

print()
t.inorder_dfs()

print()
print(inorderdfs(t))
