

def robot(moves: str):

    xMove = 0
    yMove = 0
    
    #---- move map
    # U, D = y, -y
    # R, L = x, -x

    for c in moves:
        if c == 'U':
            yMove += 1
        elif c == 'D':
            yMove -= 1
        elif c == 'R':
            xMove += 1
        else: #-- c == 'L'
            xMove -= 1
    
    if xMove == 0 and yMove == 0:
        return True
    else:
        return False

def robotoptomized(m: str):

    if m.count('L') != m.count('R') or m.count('U') != m.count('D'):
        return False
    else:
        return True


m = 'UDLR'

print(robot(m))
print(robotoptomized(m))