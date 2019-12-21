

def acfr(A: [[]]):

    Rook = 'R'
    space = '.'
    Bishop = 'B'
    pawn = 'p'

    rc = 0
    l = 0

    for r in A:
        if Rook in r:
            x, y = rc, r.index(Rook)
            break
        rc += 1
    
    #---move right
    for sq in A[x][y:]:
        if sq == Bishop:
            break
        elif sq == pawn:
            l += 1
            break

    return reversed(A[x][:y+1])

    #---move right
    for sq in A[x][:y:-1]:
        if sq == Bishop:
            break
        elif sq == pawn:
            l += 1
            break

    return l

a = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

print(acfr(a))