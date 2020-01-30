
#-- Quick sort 






import random

def quicksort(a:list):
    if len(a) <= 1:
        return a
    
    pivot = random.choice(a)
    lt = [i for i in a if i < pivot]
    eq = [i for i in a if i == pivot]
    gt = [i for i in a if i > pivot]

    return quicksort(lt) + eq + quicksort(gt)






l = []
r = 200
for _ in range(r):
    l.append(random.randrange(0,r))

print(l)
print(quicksort(l))

# -- practice

def quciksort2(a:[int]):
    if len(a) <= 1:
        return a
    
    pivot = random.choice(a)

    lt = [i for i in a if i < pivot]
    eq = [i for i in a if i == pivot]
    gt = [i for i in a if i > pivot]

    return quciksort2(lt) + eq + quciksort2(gt)

print()
print(l)
print(quciksort2(l))

