

# LeetCode: 824. Goat Latin

def toGoatLatin(S: str) -> str:
    if len(S) == 0:
        return None
    l = []
    v = ["a","e","i","o","u","A","E","I","O","U"]
    ct = 0

    for w in S.split(" "):
        ct += 1
        
        if w[:1] in v:
            l.append(w + "ma" + "a" * ct)
        else:
            l.append(w[1:] + w[:1] + "ma"+ "a" * ct)

    return " ".join(l)

s = "I speak Goat Latin"
print(toGoatLatin(s))

s = "The quick brown fox jumped over the lazy dog"
print(toGoatLatin(s))
