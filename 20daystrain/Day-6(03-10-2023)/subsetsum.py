#to check target sum is true or not
def check(arr,target,n):
    if target==0:
        return True
    if n==0 and target!=0:
        return False
    if arr[n-1]>target:
        return check(arr,target,n-1)
    return check(arr,target-arr[n-1],n-1) or check(arr,target,n-1)  
arr=list(map(int,input.split()))
target=int(input("Enter target sum:"))
n=len(arr)
print(check(arr,target,n))
