import re

def readfile(fn:str):
    pth = "D:\\Source\PythonWorkroom\\bridgewater\\" + fn
    f = open(pth, "r")
    a = [l.strip() for l in f.readlines()]
    return a
    
def generateAndPrintConcordance(inputLines):
    
    lns = inputLines.pop(0)
    a = []
    d = {}
    snt = ''
    for l in inputLines:
        for s in sentsplit(l):
            if s[len(s)-1] != '.' and s[len(s)-1] != '?' and s[len(s)-1] != '!':
                snt += ' ' + s
            else:
                a.append((snt + ' ' + s).strip())
                snt = ''
    
    for i in range(len(a)):
        for w in re.split(r'\s',a[i]):
            k = re.sub(r'[^A-Za-z]', '', w.lower())
            if k not in d:
                d[k] = conrecord(1,[str(i+1)])
            else:
                d[k].count += 1
                d[k].sentence.append(str(i+1))

    for k in sorted(d.keys()):
        snt = k + ": {" + str(d[k].count) +  ':' + ','.join(d[k].sentence) + '}'
        print(snt)

def sentsplit(s:str):
    pat = re.compile(r'[\.\?\!]\s[A-Z]')
    r = re.search(pat, s)
    a = []
    if r == None:
        a.append(s)
        return a
    else:
        return sentsplit(s[:r.start()+1]) + sentsplit(s[r.end()-1:])

class conrecord:
    def __init__(self, cnt:int, snt:[int]):
        self.count = cnt
        self.sentence = snt


tc = "testcase0"
il = readfile(tc)
print(generateAndPrintConcordance(il))
