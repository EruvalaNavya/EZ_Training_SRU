#odd magic square
n=int(input("Enter odd number magic square:"))
sq=[[0]*n for i in range(n)]
num=1
i=n//2
j=n-1
while num<=(n*n):
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
    if sq[i][j]:
        i=i+1
        j=j-2
        continue
    sq[i][j]=num
    num+=1
    i=i-1
    j=j+1
for i in sq:
    print(*i)
print("Magic constant:",n*(n*n+1)//2)
#using recursion
def generate_sq(n):
    sq=[[0]*n for i in range(n)]
    def magic(i,j,num):
        if num>(n*n):
            return sq
        if i<0 and j==n:
            i=0
            j=n-2
        else:
            if i<0:
                i=n-1
            if j==n:
                j=0
        if sq[i][j]:
            i=i+1
            j=j-2
            return magic(i,j,num)
        sq[i][j]=num
        return magic(i-1,j+1,num+1)
    return magic(n//2,n-1,1)
n=int(input("Enter odd number magic square:"))
mat=generate_sq(n)
for i in mat:
    print(*i)
print("Magic constant:",n*(n*n+1)//2)

