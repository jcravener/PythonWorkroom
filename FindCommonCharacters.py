
import re


def fcc(A: []):

    r = []
    d = {}

    for w in A:
        for c in w:
            if c not in d:
                d[c] = []
    
    for k in d.keys():
        pat = re.compile(k)
        for w in A:
            (d[k]).append(len(re.findall(pat,w)))
        for i in range(min(d[k])):
            r.append(k)
    
    return r



l = ["bella","label","roller"]
print(fcc(l))
print()
l = ["cool","lock","cook"]
print(fcc(l))
print()
l = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
print(fcc(l))
