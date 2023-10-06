#printing 1 to n using recursion
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)
n=int(input())
fun(n)
#print n to 1
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
n=int(input())
fun(n)
