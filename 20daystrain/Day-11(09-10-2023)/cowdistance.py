def isvalid(k,l,mid):
    prevcow=l[0]
    count=1
    for i in l:
        if (i-prevcow)>=mid:
            count+=1
            prevcow=i
    return True if k==count else False
def fun(k,n,l):
    l.sort()
    si=l[0]
    li=l[-1]
    res=0
    while si<=li:
        mid=(si+li)//2
        if isvalid(k,l,mid):
            res=mid
            si=mid+1
        else:
            li=mid-1
    return res
k=int(input("Enter number of cows:"))
n=int(input("Enter number of stalls:"))
l=[]
for i in range(n):
    element=input()
    l.append(element)
print(fun(k,n,l))
