
# LeetCodwe: 784. Letter Case Permutation


dp = {}

def letterCasePermutation(S: str) -> [str]:
    
    l = []

    if len(S) == 1:
        return S
    else:
        for i in range(len(S)):
            for p in letterCasePermutation(S[:i] + S[i+1:]):
                l.append(S[i] + p)
    
    return l

S = 'a1b2'

print(letterCasePermutation(S))

def caseSwap(c):
    if len(c) == 0:
        return 0
    
    o = ord(c)

    if 96 < o and o < 123:
        return chr(o-32)
    elif 64 < o and o < 90:
        return chr(o+32)
    
    return None


for c in 'ABCDEFG':
    print(caseSwap(c))



    