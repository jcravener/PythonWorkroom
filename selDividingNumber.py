
def selfdividingnumbers(left: int, right: int):

    result = []
    subresult = False

    for i in range(left, right+1):
        si = str(i)  #--cast number to str
        if "0" not in si:  #--ignore if there's a '0' in the number
            j = 0
            while j < (len(si)):
                ij = int(si[j])  #--cast curent digit to int
                if i%ij !=0:  #--if not divisable, bail to next number
                    j = len(si)
                    subresult = False
                else:
                    subresult = True
                j += 1
            if subresult == True:
                result.append(i)
                subresult = False
    
    return result

print(selfdividingnumbers(0, 2222))
