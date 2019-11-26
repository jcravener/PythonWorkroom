


def uniqueMorseRepresentations(strlst):

    morsemap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    mapscalar = 97
    result = ""
    resultset = set()

    for s in strlst:
        for c in s:
            i = ord(c) - mapscalar
            result = result + morsemap[i]
        
        resultset.add(result)
        result = ""
    
    return len(resultset)

words = ["gin", "zen", "gig", "msg"]

print(uniqueMorseRepresentations(words))