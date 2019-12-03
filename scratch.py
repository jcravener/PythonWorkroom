#
# Example 1:
#
#    Tree 1     Tree 2
#
#      1          2
#     / \        / \
#    3   2      1   3
#   /            \   \
#  5              4   7
#
#  Output:
#
#        Merged Tree
#
#            3
#           / \
#          4   5
#         / \   \
#        5   4   7














def nfactorial(n: int):

    if n == 0:
        return None
    
    if n == 1:
        return 1
    else:
        return n * nfactorial(n-1)

print(nfactorial(5))
print(1*2*3*4*5)

def fib(n):

    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


for n in range(10): print(fib(n))

print()
x = 0
x += 1
print(x)
x -= 1
print(x)


m = 'LRLLRLLR'

print(m.count('L'))

l = [[0,1,2],[3,4,5]]

print(l[:])
