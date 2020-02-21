
# LeetCode: 258. Add Digits

def addDigits(num: int) -> int:

    dgs = str(num)
    if len(dgs) == 1:
        return num
    
    nm = 0

    while len(dgs) > 1:
        nm = 0
        for d in dgs:
            nm += int(d)
        dgs = str(nm)
    
    return nm

i = 1
print(addDigits(i))