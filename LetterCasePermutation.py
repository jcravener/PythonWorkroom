
# LeetCodwe: 784. Letter Case Permutation


dp = {}

def letterCasePermutation(S: str) -> [str]:

    perm = [S]  #-- seed perm list with input string

    #-- iterate through each char in input
    for i in range(len(S)):
        #-- we're only working on alpha chars
        if S[i].isalpha():
            #-- now, we're going to work on only the existing str in the perm list
            p_len = len(perm)
            #--- for each str in per, swap case of char at the original possition
            for j in range(p_len):
                p_lst = list(perm[j])
                p_lst[i] = p_lst[i].swapcase()
                perm.append(''.join(p_lst))  #-- add result to perm list

    return perm    

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



    