#printing prime numbers in a given range
def prime(n):
    l=[True]*(n+1)
    i=2
    while(i*i<=n):
        if l[i]:
            for j in range(i*i,n+1,i):
                l[j]=False
        i+=1
    for i in range(2,n+1):
        if l[i]:
            print(i,end=" ")
n=int(input())
prime(n)

