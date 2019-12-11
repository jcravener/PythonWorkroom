


def subdomainVisit(cpdomains: []):

    h = {}
    r = []

    def updatedict(d: {}, k: str, v: int):
        if k in d:
            d[k] += v
        else:
            d[k] = v

    for e in cpdomains:
        l = e.split(" ")
        v = int(l[0])

        ll =  l[1].split('.')
        
        if len(ll) == 3:
            k = ll[2]
            updatedict(h,k,v)
            
            k = ".".join(ll[1:])
            updatedict(h,k,v)

            k = ".".join(ll)
            updatedict(h,k,v)
        else:
            k = ll[1]
            updatedict(h,k,v)

            k = ".".join(ll)
            updatedict(h,k,v)

    for key, value in h.items():
        r.append(str(value) + " " + key)
    
    return r
    
    



l = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

print(subdomainVisit(l))