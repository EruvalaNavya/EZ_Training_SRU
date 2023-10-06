#merge sort using slicing
def mergesort(l):
    if len(l)>1:
        mid=len(l)//2#taking middle element as mid
        left=l[:mid]
        right=l[mid:]
        left=mergesort(left)
        right=mergesort(right)
        merged=merge(left,right)#merging two sorted arrays
        return merged
    return l
def merge(left,right):
    res=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])#adding left remaining all elements
    res.extend(right[j:])#adding right elements
    return res
l=list(map(int,input().split()))
print(mergesort(l))
