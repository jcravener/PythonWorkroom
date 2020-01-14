
# LeetCode: 985. Sum of Even Numbers After Queries

def sumEvenAfterQueries(A: [int], queries: [[int]]) -> [int]:
    if len(A) == 0 or len(queries) == 0:
        return []
    l = []

    for q in queries:
        A[q[1]] += q[0]
        tmp = [i for i in A if i%2 == 0]
        l.append(sum(tmp))
    
    return l

A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

print(sumEvenAfterQueries(A, queries))