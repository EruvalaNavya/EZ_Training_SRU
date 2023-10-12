def backtrack(s1,s2):
    res=""
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j] and s1[i] not in res:
                res+=s1[i]
    return res
s1=input()
s2=input()
print(backtrack(s1,s2))
