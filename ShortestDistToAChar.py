
def shortestToChar(S: str, C: str):
    
    r = []
    l = []

    for i in range(len(S)):  #---Find all C
        if S[i] == C:
            l.append(i)

    for i in range(len(S)):  #--Loop through entire string
        rg = len(S) #--Set default answer for each position
        for j in l:  #--Loop through  all C positions
            #--Calulate range as the min between curent 
            # range and the dif between current C position 
            # and current S position. Need to take the 
            # absolute value of the dif because it will be 
            # negative when i > j
            rg = min(rg, abs(j - i))  
        r.append(rg)


    return r

S = "loveleetcode"
C = 'e'

print(shortestToChar(S,C))

print(S.index(C))
