def knapsack(pr,wt,sack):
    n=len(wt)
    dp=[[0 for i in range(sack+1)]for i in range(n+1)]
    for i in range(n+1):
        for w in range(sack+1):
            if w==0 or i==0:
                dp[i][w]=0
            elif wt[i-1]<=w:
                dp[i][w]=max(pr[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][sack]
pr=list(map(int,input().split()))
wt=list(map(int,input().split()))
sack=int(input())
print(knapsack(pr,wt,sack))
