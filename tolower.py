


#def tolower(s):


s = "HellO this is a tesT.  CAN YOU HEar?"
r = ''
scalar = 32

for c in s:
    if 65 <= ord(c) <= 90:
        r = r + chr(ord(c)+scalar)
    else:
        r = r + c

print(r)
    