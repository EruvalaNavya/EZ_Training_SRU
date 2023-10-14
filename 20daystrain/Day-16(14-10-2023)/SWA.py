#Sliding window algorithm
def swa(l,target):
    i=0
    j=0
    res=[l[i]]
    sum1=l[i]
    while j<len(l):
        if sum1==target:
            return res
        elif sum1<target:
            j+=1
            sum1+=l[j]
            res.append(l[j])
        else:
            res.remove(l[i])
            sum1-=l[i]
            i+=1
    return -1
l=list(map(int,input().split()))
target=int(input())
print(swa(l,target))
#i/p:2 4 6 7 8 10 ,23
#o/p:(-1),becoz it should contain continuous values

        
    
