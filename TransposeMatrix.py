

def transpose(A: [[int]]) -> [[int]]:

    l = []
    
    for i in range(len(A[0])):
        l.append([A[j][i] for j in range(len(A))])
    
    return l

a = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(a))
a = [[1,2,3],[4,5,6]]
print(transpose(a))
