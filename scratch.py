#
# Example 1:
#
#    Tree 1     Tree 2
#
#      1          2
#     / \        / \
#    3   2      1   3
#   /            \   \
#  5              4   7
#
#  Output:
#
#        Merged Tree
#
#            3
#           / \
#          4   5
#         / \   \
#        5   4   7
#
#
#
#
#
#  N-ary Tree:
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#














def nfactorial(n: int):

    if n == 0:
        return None
    
    if n == 1:
        return 1
    else:
        return n * nfactorial(n-1)

print(nfactorial(5))
print(1*2*3*4*5)

def fib(n):

    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


for n in range(10): print(fib(n))

print()
x = 0
x += 1
print(x)
x -= 1
print(x)


m = 'LRLLRLLR'

print(m.count('L'))

l = [[0,1,2],[3,4,5]]

print(l[:])


l = [-3, -1, 0, 3,5,6,-4]

print()
print(l)
l.sort()
print(l)

r = [i**2 for i in l]
r.sort()
print(r)

def revstr(s: str):
    if len(s) == 0:
        return '----'
    else:
        return revstr(s[1:]) + s[0]

print(revstr("john"))

def perm(s: str):
    
    r = []
    
    if len(s) == 1:
        return s
    else:
        for i in range(len(s)):
            for p in perm(s[:i] + s[i+1:]):
                r.append(s[i] + p)
    return r

print(perm('john'))


l = ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]

class info:
    def __init__(self):
        self.name = None
        self.count = None
    

r = []
for a in l:
    tmp = a.split(' ')
    o = info()
    o.count = tmp[0]
    o.name = tmp[1]

    r.append(o)

for e in r:
    print(e.name, e.count)

print("-" * 60)

class john:
    dp = {}

    def __init__(self,i: int):

        self.data = i

    def getdata(self):
        return self.data, self.dp

o = john(5)
print(o.getdata())


c = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"
print(len(c))
c.replace("u","")
print(len(c.replace("u","",1)))



class Solution:
    def numSmallerByFrequency(self, queries: [str], words: [str]) -> [int]:
        
        r = []
        mq = [self.freqsmall(q) for q in queries]
        mw = [self.freqsmall(w) for w in words]
        ct = 0
        
        mw.sort(reverse=True)
        
        for q in mq:
            for w in mw:
                if q < w:
                    ct += 1
                else:
                    break
            r.append(ct)
            ct = 0

            
        return r
        
    def freqsmall(self, s:str) -> int:
        mn = min(s)       
        return s.count(mn)

q = ["bbb","cc"]
w = ["a","aa","aaa","aaaa"]
s = Solution()
print(s.numSmallerByFrequency(q,w))