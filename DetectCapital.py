

# LeetCode: 520. Detect Capital

def detectCapitalUse(word: str) -> bool:

    sortedWord = sorted(word)
    if ord(sortedWord[0]) >= 65 and ord(sortedWord[len(sortedWord)-1]) <= 90:
        return True
    
    if ord(sortedWord[0]) >= 97 and ord(sortedWord[len(sortedWord)-1]) <= 122:
        return True
    
    if ord(word[0]) >= 65 and ord(word[0]) <= 90:
        sortedWord = sorted(word[1:])
        if ord(sortedWord[0]) >= 97 and ord(sortedWord[len(sortedWord)-1]) <= 122:
            return True
    
    return False

i = "USA"
print(detectCapitalUse(i))
i = "John"
print(detectCapitalUse(i))
i = "coffee"
print(detectCapitalUse(i))
i = "CofFee"
print(detectCapitalUse(i))
