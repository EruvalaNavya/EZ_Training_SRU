def sum_ele(arr,si,li):
    if si==li:
        return arr[si]
    mid=(si+li)//2
    return sum_ele(arr,si,mid)+sum_ele(arr,mid+1,li)
arr=list(map(int,input().split()))
print(sum_ele(arr,0,len(arr)-1))
