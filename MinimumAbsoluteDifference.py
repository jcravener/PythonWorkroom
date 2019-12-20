


def mad(arr: []):
    arr.sort()
    d = {}
    lowest = arr[1] - arr[0]

    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if diff < lowest:
            lowest = diff
        if diff not in d:
            d[diff] = [[arr[i],arr[i+1]]]
        else:
            (d[diff]).append([arr[i],arr[i+1]])

    return d[lowest]

arr = [4,2,1,3]
print(mad(arr))
arr = [1,3,6,10,15]
print(mad(arr))
arr = [3,8,-10,23,19,-4,-14,27]
print(mad(arr))

def perm(s: str):
    if len(s) == 1:
        return s
    
    r = []

    for i in range(len(s)):
        for p in perm(s[:i] + s[i+1:]):
            r.append(s[i] + p)
    
    return r

s = 'abc'
print(perm(s))