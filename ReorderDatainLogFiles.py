
# LeetCode: 937. Reorder Data in Log Files

def reorderLogFiles(logs: [str]) -> [str]:
    
    let = [l for l in logs if not (l.split(' ')[1]).isdecimal()]
    let = sorted(let, key=lambda x: x.split(" ", 1)[0])
    let = sorted(let, key=lambda x: x.split(" ", 1)[1])
    
    let.extend([l for l in logs if (l.split(' ')[1]).isdecimal()])
    return let

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
print(reorderLogFiles(logs))

