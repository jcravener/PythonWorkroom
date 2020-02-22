

# LeetCode: 953. Verifying an Alien Dictionary

def isAlienSorted(words: [str], order: str) -> bool:
    aorder = list(order)
    minlen = max([len(w) for w in words])
    tmp = []
    l = []

    for i in range(minlen):
        for w in words:
            if i < len(w):
                tmp.append(aorder.index(w[i]))
            else:
                tmp.append(-1)
        l.append(tmp)
        tmp = []

    return l


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(isAlienSorted(words, order))
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(isAlienSorted(words, order))

