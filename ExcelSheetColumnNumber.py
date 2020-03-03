


# LeetCode: 171. Excel Sheet Column Number

def titleToNumber(s: str) -> int:
    
    sl = list(s)
    
    cur = ''
    num = 0
    i = 0

    while len(sl) != 0:
        cur = sl.pop()
        num += (ord(cur)-64) * 26**i
        i += 1

    return num



print(titleToNumber('ZY'))
