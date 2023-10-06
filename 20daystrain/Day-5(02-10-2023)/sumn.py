
#print sum of didgits
def fun(n):
    if n<=1:
        return n
    else:
        return n+fun(n-1)
n=int(input())
print(fun(n))
