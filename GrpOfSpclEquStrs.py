


def numSpecialEquivGroups(A: [str]):    
    st = set()

    for s in A:
        k = ''.join(sorted(s[::2])) + ''.join(sorted(s[1::2]))
        st.add(k)

    return len(st)

a = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
print(numSpecialEquivGroups(a))

a = ["abc","acb","bac","bca","cab","cba"]
print(numSpecialEquivGroups(a))

