# LeetCode: 682. Baseball Game

def calPoints(ops:[str]) -> int:
    p = "+DC"
    valpts = []

    for i in ops:
        if i not in p:
            valpts.append(int(i))
        elif i == "+":
            valpts.append(sum(valpts[-2:]))
        elif i == "D":
            valpts.append(valpts[len(valpts)-1] * 2 )
        elif i == "C":
            valpts.pop()
    
    return sum(valpts)

ip = ["5","2","C","D","+"]
print(calPoints(ip))
print()

ip = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ip))
print()


