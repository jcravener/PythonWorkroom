


def numUniqueEmails(emails: [str]):
    
    s = set()
    for a in emails:
        localname = a.split('@')[0]
        domainname = a.split('@')[1]
        filtername = localname.split('+')[0]        

        forwardname = filtername.replace('.','')
        
        s.add(forwardname + "@" + domainname)

    return s

l = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

print(numUniqueEmails(l))
