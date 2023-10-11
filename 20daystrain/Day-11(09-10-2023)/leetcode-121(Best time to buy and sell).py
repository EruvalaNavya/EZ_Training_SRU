class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp,buy=0,prices[0]
        for i in prices:
            if i<buy:
                buy=i
            elif (i-buy)>maxp:
                maxp=(i-buy)
        return maxp
