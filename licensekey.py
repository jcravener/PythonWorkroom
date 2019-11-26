

def formatkey(keystring="",k=4):

    groupcount = int(k)
    result = ""
    ksupper = keystring.upper()

    charcount = 0

    for i in range(len(ksupper)-1,-1, -1):
        
        if ksupper[i] == "-":
            continue

        charcount += 1
        
        result = ksupper[i] + result

        if charcount == groupcount:
            result = "-" + result
            charcount = 0
        
    return result

s = "asdd837-s-f-f-erfkkf9-sjfhty-f-f-f-f-"

print(formatkey(s,5))

