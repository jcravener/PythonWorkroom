
# LeetCode: 762. Prime Number of Set Bits in Binary Representation

def countPrimeSetBits(L: int, R: int) -> int:
    if L < 1:
        return 0
    if R < L:
        return 0
    tot = 0
    
    for i in range(L,R+1):
        s = bin(i)
        if isPrime( s.count('1') ):
            tot += 1
    
    return tot
    
def isPrime(n:int):
    if n < 2:
        return False
    
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

print(countPrimeSetBits(10,15))

