
def lettercombos(digits):
    outputlist = []

    if len(digits) == 0:
        return outputlist
    
    outputlist.append("")

    charmap = [0,1,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

    for i in range(len(digits)):
        index = int(digits[i])

        while len(outputlist[0]) == i:
            permutation = outputlist.pop(0)

            for c in charmap[index]:
                outputlist.append(permutation + c)
    
    return outputlist

d = '232'

print(lettercombos(d))
