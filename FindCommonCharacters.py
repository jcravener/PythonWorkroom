
def fcc(A: []):

    l = []

    for w in A:
        d = {}
        for c in w:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        l.append(d)
    
    dd = {}

    for d in l:
        for k,v in d.items():
            if k not in dd:
                
    
    return l



                
        

l = ["bella","label","roller"]
print(fcc(l))
print()
l = ["cool","lock","cook"]
print(fcc(l))
print()
l = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
print(fcc(l))
