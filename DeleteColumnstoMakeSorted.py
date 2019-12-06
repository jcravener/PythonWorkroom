

def minDeletionSize(A):

    D = []

    if len(A[0]) == 1:
        return D

    for c in range(len(A[0])):
        prev_c = ord(A[0][c])
        for r in range(len(A)):
            cur_c = ord(A[r][c])
            if cur_c < prev_c:
                D.append(c)
                break
            prev_c = cur_c
    return D

#A = ["cba","daf","ghi"]
#A = ["a", "b"]
A = ["zyx","wvu","tsr"]
A = ["rrjk","furt","guzm"]

print(minDeletionSize(A))


