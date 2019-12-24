import re

def removeDuplicates(S: str):

    s = S
    pat = re.compile(r'(.)\1')

    while re.search(pat, s):
        s = re.sub(pat,'',s)
    return s

def removeDuplicatesStack(S: str):

    s = []

    for c in S:
        if not s or c != s[-1]:
            s.append(c)
        else:
            s.pop()
    return ''.join(s)

s = 'aaaaaaa'
print(removeDuplicates(s))
print(removeDuplicatesStack(s))