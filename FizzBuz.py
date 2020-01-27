

# LeetCode: 412. Fizz Buzz

def fizzBuzz(n: int) -> [str]:

    r = []

    for v in range(1,n+1):
        if v%3 == 0 and v%5 == 0:
            r.append("FizzBuzz")
        elif v%3 == 0:
            r.append("Fizz")
        elif v%5 == 0:
            r.append("Buzz")
        else:
            r.append(str(v))
    
    return r

n = 15
print(fizzBuzz(n))