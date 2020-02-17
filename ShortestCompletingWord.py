


# LeetCode: 748. Shortest Completing Word

def shortestCompletingWord(licensePlate: str, words: [str]) -> str:
    lt = [c.lower() for c in licensePlate if c.isalpha()]
    r = ''
    tmp = []
    ct = 0

    for w in words:
        tmp = list(w)
        ct = 0

        for l in lt:
            if l in tmp:
                tmp.remove(l)
                ct += 1
            else:
                break
        
        if ct == len(lt):
            if r == '' or len(w) < len(r):
                r = w
        
    return r

lp = "1s3 PSt"
w = ["step", "steps", "stripe", "stepple"]
lp = "1s3 456"
w =  ["looks", "pest", "stew", "show"]

print(shortestCompletingWord(lp, w))
