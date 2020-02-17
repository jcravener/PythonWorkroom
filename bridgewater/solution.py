import re

def readfile(fn:str):
    pth = "D:\\Source\PythonWorkroom\\bridgewater\\" + fn
    f = open(pth, "r")
    a = [l.strip() for l in f.readlines()]
    return a
    

def generateAndPrintConcordance(inputLines):
    
    a = []
    for l in inputLines:
        a.extend(sentsplit(l))
    
    return a

def sentsplit(s:str):
    pat = re.compile(r'[\.\?\!]\s[A-Z]')
    r = re.search(pat, s)
    a = []
    if r == None:
        a.append(s)
        return a
    else:
        return sentsplit(s[:r.start()+1]) + sentsplit(s[r.end()-1:])


tc = "testcase0"
il = readfile(tc)
print(generateAndPrintConcordance(il))

s = "Wait a minute. Wait a minute, Doc. Just wait a minute! Hold on!!"
s = 'This is not'
#pat = re.compile(r'[\.\?\!]\s[A-Z]')
#r = re.search(pat,s)

#print(sentsplit(s))
