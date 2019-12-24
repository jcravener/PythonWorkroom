


def findOcurrences(text: str, first: str, second: str):

    l = text.split()
    r = []

    for i in range(len(l)):
        if i+2 <= len(l) - 1 and l[i] == first and l[i+1] == second:
            r.append(l[i+2])

    return r

text = "we will we will rock you"
first = "we"
second = "will"

text = "alice is a good girl she is a good student"
first = "a"
second = "good"

text = "we will we will rock you"
first = "we"
second = "will"

print(findOcurrences(text, first, second))

        