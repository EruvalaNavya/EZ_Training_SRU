def fib(n,dp):
    if dp[n]:
        return dp[n]
    if n==0:
        dp[0]=0
        return 0
    if n==1:
        dp[1]=1
        return 1
    dp[n]=fib(n-1,dp)+fib(n-2,dp)
    return dp[n]
n=int(input("Enter index value of fibonacci number to know:"))
dp=[0]*(n+1)
fib(n,dp)
print("Fibonacci series:",dp)
print("Value at given index:",dp[n])
