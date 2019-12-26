
class node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def getleaves(r: node):

    l = []
    q = [r]
    lv = []

    while q:
        cur_node = q.pop(0)

        l.append(cur_node.value)
        
        if cur_node.left == None and cur_node.right == None:
            lv.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    
    return l, lv


def getleavesdfs(r:node):

    lv = []

    if r.left:
        lv = getleavesdfs(r.left)
    if r.left == None and r.right == None:
        lv.append(r.value)
    if r.right:
        lv = lv +  getleavesdfs(r.right)
    
    return lv


r = node(3)
r.left = node(5)
r.right = node(1)

(r.left).left = node(6)
(r.left).right = node(2)
((r.left).right).left = node(7)
((r.left).right).right = node(4)

(r.right).left = node(9)
(r.right).right = node(8)

print(getleaves(r))

print(getleavesdfs(r))

