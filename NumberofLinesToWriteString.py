


def numberOfLines( widths: [int], S: str):

    idx_offset = 97
    max_line_width = 100
    w = 0
    linecount = 0

    for c in S:
        idx = ord(c) - idx_offset
        w += widths[idx]
        if w == max_line_width:
            linecount += 1
            w = 0
        elif w > max_line_width:
            linecount +=1
            w = widths[idx]
    
    return [linecount+1, w]


widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"

print(numberOfLines(widths,S))

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"

print(numberOfLines(widths,S))

