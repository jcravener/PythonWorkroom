

# LeetCode: 1071. Greatest Common Divisor of Strings

def gcdOfStrings(str1: str, str2: str) -> str:

    ln1 = len(str1)
    ln2 = len(str2)

    if ln1 > ln2:
        big = str1
        small = str2
    else:
        big = str2
        small = str1
    
    s = ''
    p = ''
    bst = set()
    sst = set()

    for c in small:
        p += c
        bst = set(big.split(p))
        sst = set(small.split(p))

        if (len(bst) == 1 and len(sst) == 1) and (bst == sst):
            s = p
   
    return s

str1 = "ABCABC"
str2 = "ABC"
#str1 = "ABABAB"
#str2 = "ABAB"
#str1 = "LEET"
#str2 = "CODE"
str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

print(gcdOfStrings(str1, str2))


