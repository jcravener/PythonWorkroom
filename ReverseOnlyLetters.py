
# LeetCode: 917. Reverse Only Letters

def reverseOnlyLetters(S: str) -> str:

    slst = list(S)
    a = []

    for i in range(len(slst)):
        if (slst[i]).isalpha():
            a.append(slst[i])
            slst[i] = None

    for i in range(len(slst)):
        if slst[i] == None:
            slst[i] = a.pop()

    return "".join(slst)

s = "a-bC-dEf-ghIj"
#s = "Test1ng-Leet=code-Q!"
print(reverseOnlyLetters(s))