

def removeouterparen(s: str):

    if s == None:
        return None
    
    ocount = 0
    ccount = 0
    primative = ""
    result = ""

    for c in s:
        
        primative += c
        
        if c == "(":
            ocount += 1
        else:
            ccount += 1
        
        if ocount == ccount:
            result += primative[1:len(primative)-1]
            ocount = 0
            ccount = 0
            primative = ""
    
    return result

#-------------------------------------------------------------------

s = "(()())(())"
print(removeouterparen(s))

print("")
s = "(()())(())(()(()))"
print(removeouterparen(s))

print("")
s = "()()"
print(removeouterparen(s))
