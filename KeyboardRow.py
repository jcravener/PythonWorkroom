
def findWords(words: [str]) -> [str]:

    if len(words) == 0:
        return []

    kb = ['qwertyuiop','asdfghjkl','zxcvbnm']

    l = []

    for r in kb:
        for w in words:
            if fndwrd(w, r):
                l.append(w)
    return l

def fndwrd(wrd: str, row: str):
    for c in wrd.lower():
        if c not in row:
            return False
    return True

a = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(a))

