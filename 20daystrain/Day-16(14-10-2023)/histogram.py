l=list(map(int,input().split()))
var=max(l)
n=len(l)
'''sp=[0]*n
for i in range(n):
    sp[i]=(var-l[i])
for j in range(var):
    for i in range(n):
        if sp[i]==0:
            print("*",end=' ')
        else:
            print(" ",end=' ')
            sp[i]-=1
    print()
for i in range(n):
    print("*"*l[i])'''
for i in range(var,0,-1):
    print(f"{i:2d} | ",end="")
    for j in l:
        if j>=i:
            print("X",end=' ')
        else:
            print(" ",end=' ')
    print()
#o/p:2 3 0 4 6 3 2 1
''' 6 |         X       
    5 |         X       
    4 |       X X       
    3 |   X   X X X     
    2 | X X   X X X X   
    1 | X X   X X X X X '''
