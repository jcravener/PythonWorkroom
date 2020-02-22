

# LeetCode: 696. Count Binary Substrings
#
#  The idea here is to count up batches of characters.
#  
#  Once you have a full batch of both characteres, 
#  caclulate the min len value between the 2 to get the 
#  total substring count of those batches. E.g. 
#  '00011' = '000' in one batch and '11' in another.
#  The min value between these two is 2, which equals
#  the number of subsctrings - '0011' and '01'
#  
#  Once you do a min calc of 2 batches, move on to
#  the next two by switching the current batch with
#  the previous one and start over. You know to
#  start over once you have switched charaters after
#  having 2 batchesd already. When you get to this point
#  you would have seen a 3rd char i.e. '0' '1' '0'
#  
#  Once you're done with the entire string, you also
#  need to cal the min value between the last two
#  batches. This is becuse you will break out of
#  loop before getting a chance to calulate them   

def countBinarySubstrings(s: str) -> int:
    if len(s) == 0:
        return 0

    curc = s[0]
    curct = 1
    prevct = 0
    ct = 0

    for c in s[1:]:
        if c == curc:
            curct += 1
        else:
            #if prevct:
            ct += min(prevct, curct)
            prevct = curct
            curct = 1
            curc = c
    
    ct += min(prevct, curct)

    return ct


#s = '00110011'
s = '10101'
print(countBinarySubstrings(s))