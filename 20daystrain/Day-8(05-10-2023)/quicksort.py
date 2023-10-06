#quick sort using recursion
def fun(arr,start,end):
    if start<end:
        piv=qsort(arr,start,end)
        fun(arr,start,piv-1)#left part
        fun(arr,piv+1,end)#right part
def qsort(arr,start,end):
    piv=arr[end]
    i=start-1
    for j in range(start,end):
        if arr[j]<piv:
            i=i+1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[end]=arr[end],arr[i+1]
    return i+1
arr=list(map(int,input().split()))
fun(arr,0,len(arr)-1)
for i in range(len(arr)):
    print(arr[i],end=' ')
