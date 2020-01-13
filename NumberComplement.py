
# LeetCode: 476. Number Complement

def findComplement(num: int) -> int:

    bn = bin(num)
    cn = ''

    for b in bn[2:]:
        if b == '0': cn += '1'
        else: cn += '0'
    #cn = '0b' + cn


    return int(cn, 2)

print(findComplement(5))
print(findComplement(1))