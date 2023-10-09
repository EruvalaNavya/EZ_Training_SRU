#Knapsack problem using greedy algorithm
kwt=int(input("Enter knapsack bag capacity:"))
print("Enter knapsack weights:")
wt=list(map(int,input().split()))
print("Enter profit:")
pt=list(map(int,input().split()))
l=list(zip(wt,pt))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
maxpr=0
for weight,profit in l:
    if weight<=kwt:
        maxpr+=profit
        kwt-=weight
    else:
        maxpr+=kwt*(profit/weight)
        break
print("Maximum profit is:",maxpr)
'''            
o/p:
Enter knapsack bag capacity:30
Enter knapsack weights:
20 10 5 15 25
Enter profit:
100 75 40 55 65
Maximum profit is: 190.0'''
