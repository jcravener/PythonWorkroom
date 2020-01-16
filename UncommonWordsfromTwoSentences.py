

# LeetCode: 884. Uncommon Words from Two Sentences
# My first solution used a dictionary, and was only 89% fast.
# This one uses the list count method and did not prove
# faster per multiple submissions. However, the speed rating
# kept varying widely (?). This one uses less code than the first.

def uncommonFromSentences(A: str, B: str) -> [str]:

    a = A.split(' ') + B.split(' ')
    l = []

    for i in a:
        if a.count(i) == 1:
            l.append(i)

    return l

A = "this apple is sweet"
B = "this apple is sour"
print(uncommonFromSentences(A,B))
print()

A = "apple apple"
B = "banana"
print(uncommonFromSentences(A,B))
