


def sortArrayByParityII(A: [int]):
    
    r = []
    odds = []
    evens = []

    for n in A:
        if n%2 == 0:
            evens.append(n)
        else:
            odds.append(n)

    for e in evens:
        r.append(e)
        r.append(odds.pop())
    
    return r


l = [80,10,8,44,4,2,5,7,33,11,9,17]
#l = [17,80]
#l = [4,1,2,1]

print(sortArrayByParityII(l))
