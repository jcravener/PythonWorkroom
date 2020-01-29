

# LeetCode: 824. Goat Latin

def toGoatLatin(S: str) -> str:
    if len(S) == 0:
        return None
    l = []
    v = ["a","e","i","o","u"]
    c = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    ct = 0

    for w in S.split(" "):
        ct += 1
        
        if (w[:1]).lower() in v:
            l.append(w+ "ma" + "a" * ct)
        elif (w[:1]).lower() in c:
            l.append(w[1:] + w[:1] + "ma"+ "a" * ct)

    return " ".join(l)

s = "I speak Goat Latin"
print(toGoatLatin(s))

s = "The quick brown fox jumped over the lazy dog"
print(toGoatLatin(s))
