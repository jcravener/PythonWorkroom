def diStringMatch(s: str):

    result = []

    Icount = 0
    Dcount = len(s)
    
    for c in s:
        if c == 'I':
            result.append(Icount)
            Icount += 1
        else:
            result.append(Dcount)
            Dcount -= 1
    
    if c == 'I':
        result.append(Icount)
    else:
        result.append(Dcount)
    
    return result

sl = ["IDID", "III", "DDI"]

for s in sl: print(diStringMatch(s))

