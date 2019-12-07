


class ntree:
    def __init__(self, data=None):
        self.data = data
        self.children = []
    
    def addchild(self, data):
        cur_node = self
        new_node = ntree(data)        
        cur_node.children.append(new_node)
    
    def getroot(self):
        return self.data
    
    def getchildren(self):
        l = []
        for c in self.children:
            l.append(c.data)
        return l
    
    def traverse(self):
        r = []
        q = [self]

        while q:
            cur_node = q.pop()
            
            if cur_node:  #-- not sure why I have to do this check but LeetCode faild the 2nd testcase withou it.  Not sure how a you would instatiate a None ntree
                r.append(cur_node.data)

                if cur_node.children:
                    for c in cur_node.children:
                        q.append(c)
    
        return r[::-1]

    def recurse_traverse(self):  #-- now need to do a recursive implmentation.
        cur_node = self

        if not cur_node:
            return []
        
        r = [cur_node.data]

        def helper(nd: ntree):
            
            for c in nd.children:
                r.append(c.data)
                helper(c)
        
        helper(cur_node)
        return r

nt = ntree(10)
for d in range(5,9,1): nt.addchild(d)
for d in range(0,4,1): (nt.children[0]).addchild(d)
print(nt.traverse())
print(nt.recurse_traverse())
