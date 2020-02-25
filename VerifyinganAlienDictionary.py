

# LeetCode: 953. Verifying an Alien Dictionary

def isAlienSorted(words: [str], order: str) -> bool:

    v = 65
    d = {}
    map = []
    s = ''
    for k in order:
        d[k] = chr(v)
        v += 1
    
    for w in words:
        for c in w:
            s += d[c]
        map.append(s)
        s = ''

    return map == sorted(map)


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))
print()
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(isAlienSorted(words, order))
print()
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(isAlienSorted(words, order))
print()
words = ["kuvp","q"]
order = "ngxlkthsjuoqcpavbfdermiywz"
print(isAlienSorted(words, order))
print()
