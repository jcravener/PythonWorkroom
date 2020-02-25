

# LeetCode: 13. Roman to Integer

def romanToInt(s: str) -> int:
    d = {}
    d['I'] = 1
    d['V'] = 5
    d['X'] = 10
    d['L'] = 50
    d['C'] = 100
    d['D'] = 500
    d['M'] = 1000
    
    ds = {}
    ds['IV'] = 4
    ds['IX'] = 9
    ds['XL'] = 40
    ds['XC'] = 90
    ds['CD'] = 400
    ds['CM'] = 900

    tot = 0

    for k in ds:
        s = s.replace(k, '+' + str(ds[k]) + '+')
    for v in [i for i in s.split('+') if i != '']:
        if v.isdecimal():
            tot += int(v)
        else:
            for c in v:
                tot += d[c]
    
    return tot

ip = ['III','IV','IX','LVIII','MCMXCIV',]

for s in ip:
    print(romanToInt(s))
    