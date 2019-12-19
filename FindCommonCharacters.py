



def fcc(A: []):

    d = dict()
    l_len = len(A)
    r = []

    for w in A:
        for c in w:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
            
    for i in d.items():
        k, v = i
        if v < l_len: continue
        for n in range(v//l_len):
            r.append(k)
            print(i)
    
    return r

l = ["bella","label","roller"]
print(fcc(l))
print()
l = ["cool","lock","cook"]
print(fcc(l))
print()
l = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
print(fcc(l))
