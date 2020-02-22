

# LeetCode: 696. Count Binary Substrings

def countBinarySubstrings(s: str) -> int:
    if len(s) == 0:
        return 0

    curc = s[0]
    curct = 1
    oldct = 0
    ct = 0

    for c in s[1:]:
        if c == curc:
            curct += 1
        else:
            if oldct:
                ct += min(oldct, curct)
            oldct = curct
            curct = 1
            curc = c
    ct += min(oldct, curct)

    return ct


s = '00110011'
#s = '10101'
print(countBinarySubstrings(s))