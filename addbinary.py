
# 101
# 100
#----
#1001

import re

def addbinary(s1,s2):

    p = re.compile('^[01]+$')

    if not p.match(s1):
        return 0

    if not p.match(s2):
        return 0

    if len(s1) > len(s2):
        s2 = s2.zfill(len(s1))
    elif len(s2) > len(s1):
        s1 = s1.zfill(len(s2))
    
    #return [s1, s2]

    sum = ''
    cary = False

    for i in range(len(s1)-1, -1, -1):
        if s1[i] == s2[i] and s1[i] == '1':  # 1+1 = 10
            if cary: # 1+1+1 = 11
                sum  = '1' + sum 
                cary = True
            else: # 1+1 = 1
                sum = '0' + sum 
                cary = True
        elif s1[1] == s2[i] and s1[i] == '0': # 0+0 = 0
            if cary: # 1+0+0 = 1
                sum = '1' + sum
                cary = False
            else: # 0+0 = 0
                sum = '0' + sum
                cary = False
        else: # 0+1 = 1
            if cary: # 1+0+1 = 10
                sum = '0' + sum
                cary = True
            else: # 0+1 = 1
                sum = '1' + sum
                cary = False

    if cary:
        sum = '1' + sum
       
    return sum

a1 =   "01011"
a2 = "1010111"

print(addbinary(a1,a2))

print(5//2)
print(5%2)