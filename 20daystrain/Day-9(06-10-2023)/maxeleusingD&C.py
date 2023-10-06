def max_ele(arr,si,li):
    if si==li:
        return arr[si]
    mid=(si+li)//2
    #return max(max_ele(arr,si,mid),max_ele(arr,mid+1,li))
    return max_ele(arr,si,mid)if(max_ele(arr,si,mid)>max_ele(arr,mid+1,li))else max_ele(arr,mid+1,li)
arr=list(map(int,input().split()))
print(max_ele(arr,0,len(arr)-1))
