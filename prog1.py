

fib_cache = {}

def fib(n):
    
    if n in fib_cache:
        return fib_cache[n]

    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        v = fib(n-2) + fib(n-1)
    
    fib_cache[n] = v
    return v

for i in range(0,1):
    print(fib(i))


a = [1,2,3,4]



s = ["abc","sdfe", "22234"]

print(len(s[-1]))
