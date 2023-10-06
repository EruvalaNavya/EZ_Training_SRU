#insertion sort
l=list(map(int,input().split()))
n=len(l)
for i in range(1,n):
    key=l[i]
    j=i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
for i in range(n):
    print(l[i],end=" ")
#using 1 for loop
'''def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j-1] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j-1
    return arr
arr = [7,-1,0,5,2]
ans = insertion_sort(arr)
print(ans)'''
