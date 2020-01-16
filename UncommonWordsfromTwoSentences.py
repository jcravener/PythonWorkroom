

# LeetCode: 884. Uncommon Words from Two Sentences

def uncommonFromSentences(A: str, B: str) -> [str]:

    d = {}

    for i in ( A.split(' ') + B.split(' ') ):
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    return [k for k, v in d.items() if v == 1]

A = "this apple is sweet"
B = "this apple is sour"
print(uncommonFromSentences(A,B))
print()

A = "apple apple"
B = "banana"
print(uncommonFromSentences(A,B))
