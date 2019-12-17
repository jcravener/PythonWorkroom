class node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def display(nd: node):
    return inoder_dsf(nd)

def inoder_dsf(nd: node):
    if nd.left:
        inoder_dsf(nd.left)
    return nd.val
    if nd.right:
        inoder_dsf(nd.right)


nd = node(5)
nd.left = node(3)
nd.right = node(6)


print(inoder_dsf(nd))
