


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
        
        print(self.data)

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





#------------------------------------------------------------------------

t = tree(10)
t.insert_left(9)
t.insert_right(12)
t.insert_left(8)
t.insert_right(13)

t.preorder_dfs()

print()
t.inorder_dfs()

print()
t.postorder_dfs()

print()
t.bfs()