l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            c+=1
print("Inversion count of given array:",c)
