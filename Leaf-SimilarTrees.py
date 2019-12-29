
class node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def getleaves(r: node):

    if not r:
        return []
    
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
    
    return lv


def getleavesdfs(r:node):

    if not r:
        return []
    
    lv = []

    if r.left:
        lv = getleavesdfs(r.left)
    if r.left == None and r.right == None:
        lv.append(r.value)
    if r.right:
        lv = lv +  getleavesdfs(r.right)
    
    return lv

def leafSimilar(root1: node, root2: node):
    
    if root1 == None and root2:
        return False
    if root2 == None and root1:
        return False
    
    #---bsf will not work becuse it doesn't preserver the order accross trees.
    #lv1 = getleaves(root1) 
    #lv2 = getleaves(root2)
    lv1 = getleavesdfs(root1)
    lv2 = getleavesdfs(root2)

    if len(lv1) != len(lv2):
        return False
    
    for i in range(len(lv1)):
        if lv1[i] != lv2[i]:
            return False
    
    return True



r = node(3)
r.left = node(5)
r.right = node(1)

(r.left).left = node(6)
(r.left).right = node(2)
((r.left).right).left = node(7)
((r.left).right).right = node(4)

(r.right).left = node(9)
(r.right).right = node(8)

print(getleaves(r.left))
print(getleavesdfs(r.right))

print(leafSimilar(r.left, r.right))

a = [i for i in range(10)]
b = [i for i in range(10)]

if a == b:
    print(a,b)



