#take binary matrix as input where 0->water,1->land;print no.of islands=? where 1's are surrounded by 0's
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
    if j>0:
        fun(l,i,j-1,n)
    if j<n-1:
        fun(l,i,j+1,n)
    if i>0:
        fun(l,i-1,j,n)
    if i<n-1:
        fun(l,i+1,j,n)
l=[]
n=int(input("Enter matrix size:"))
for i in range(n):
    l.append(list(map(int,input().split())))
c=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            c=c+1
            fun(l,i,j,n)
print(c)

output:
    4
    1 0 0 1
    1 0 0 0
    1 0 1 0
    0 1 1 1
    2
