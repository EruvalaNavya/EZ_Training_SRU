#using 1 function and invrersion count
def mergesort(l,inv):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        li=mergesort(left,inv)#li-left inversion
        ri=mergesort(right,inv)#right inversion
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                l[k]=left[i]
                i+=1
                k+=1
            else:
                l[k]=right[j]
                j+=1
                k+=1
                inv+=(len(left)-i)
        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1
        return li+ri+inv
    return 0
l=list(map(int,input().split()))
print("Inversion count:",mergesort(l,0))
print(l)

        
