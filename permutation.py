

def perm(s: str):
    if len(s) == 1:
        return s
    
    results = []

    for i in range(len(s)):
        for p in perm(s[:i]+s[i+1:]):
            results.append(s[i] + p)
    
    return results

s = 'abc'

print(perm(s))



