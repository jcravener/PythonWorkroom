






def nfactorial(n: int):

    if n == 0:
        return None
    
    if n == 1:
        return 1
    else:
        return n * nfactorial(n-1)

print(nfactorial(5))
print(1*2*3*4*5)

