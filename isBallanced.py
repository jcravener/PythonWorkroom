
def isBallanced(matrix: []):

    if len(matrix) == 0:
        return False

    stk = []
    opn = '('
    
    for r in matrix:
        for e in r:
            if e == opn:
                stk.append(opn)
            else:
                if len(stk) == 0:
                    return False
                else:
                    stk.pop()                
    if len(stk) == 0:
        return True
    else:
        return False

m0 = []  # false
m1 = [["(","("],[")",")"]]; # true
m2 = [[")","(",")"],["(","(",")"]]; # false
m3 = [["(","(",")"],["(",")",")"]]; # true
m4 = [["(","(",")"],["(",")",")"],["(","(","("]]; # false
m5 = [[")",")",")"],[")",")",")"]]; # false
m6 = [["(","(","("],[")",")",")"]]; # true
m7 = [[")","(","("],[")","(","("]]; # false
m8 = [["(","(","(","("],[")","(",")","("],[")",")",")",")"]]; # true

print(0, isBallanced(m0))
print(1, isBallanced(m1))
print(2, isBallanced(m2))
print(3, isBallanced(m3))
print(4, isBallanced(m4))
print(5, isBallanced(m5))
print(6, isBallanced(m6))
print(7, isBallanced(m7))
print(8, isBallanced(m8))
