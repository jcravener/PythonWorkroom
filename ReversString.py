
# -- Cannot use another array

def reverseString( s: [str]):

    for i in range(len(s)//2):        
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
    
    return s

s = 'helloworld'
a = [c for c in s]

print(reverseString(a))
