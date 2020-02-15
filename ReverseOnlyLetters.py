
# LeetCode: 917. Reverse Only Letters

def reverseOnlyLetters(S: str) -> str:

    slst = list(S)
    li = 0
    ri = len(slst) - 1

    while li <= ri:
        l = slst[li]
        r = slst[ri]

        if l.isalpha() and r.isalpha():
            slst[li], slst[ri] = slst[ri], slst[li]
            li += 1
            ri -= 1
        elif l.isalpha() and (not r.isalpha()):
            ri -= 1
        elif (not l.isalpha()) and r.isalpha():
            li += 1
        else:
            li += 1
            ri -= 1

    return "".join(slst)

s = "a-bC-dEf-ghIj"
s = "Test1ng-Leet=code-Q!"
print(reverseOnlyLetters(s))