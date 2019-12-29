def allCellsDistOrder(R: int, C: int, r0: int, c0: int) -> [[int]]:

    r = 0
    c = 0
    l = []
    d = {}

    for r in range(R):
        for c in range(C):
            k = abs(r0 - r) + abs(c0 - c)
            if k not in d:
                d[k] = [[r,c]]
            else:
                d[k] += [[r,c]]
    
    for k in sorted(d.keys()):
        for e in d[k]:
            l.append(e)
    
    return l

R = 1
C = 2
r0 = 0
c0 = 0
print(allCellsDistOrder(R, C, r0, c0))
print()

R = 2
C = 2
r0 = 0
c0 = 1
print(allCellsDistOrder(R, C, r0, c0))
print()

R = 2
C = 3
r0 = 1
c0 = 2
print(allCellsDistOrder(R, C, r0, c0))
print()
