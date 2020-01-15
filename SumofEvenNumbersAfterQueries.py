
# LeetCode: 985. Sum of Even Numbers After Queries
# Solution was in LeetCode dicussions...
# My first attempt worked, but was too slow with large test cases

def sumEvenAfterQueries(A: [int], queries: [[int]]) -> [int]:
    if len(A) == 0 or len(queries) == 0:
        return []
    
    l = []
    cur_sum = sum([i for i in A if i%2 == 0])
    
    for q in queries:
        if A[q[1]]%2 == 0: #-- if even, it's alredy in cur_sum
            if q[0]%2 == 0:  #-- if the addition ends up even, need to add to cur_sum
                cur_sum += q[0]
            else:  #-- if the addtion is not even, need to subtract the sum
                cur_sum -= A[q[1]]
        else:  #-- if odd it's not in cur_sum
            if q[0]%2 != 0: #-- both are odd, making even so needs to be added to sum
                cur_sum += A[q[1]] + q[0]
        
        #---now update list and just go back, working with the latess sum
        A[q[1]] += q[0]
        l.append(cur_sum)
    
    return l

A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

print(sumEvenAfterQueries(A, queries))

