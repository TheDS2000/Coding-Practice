https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = prices[-1]
        profit = 0
        for i in range(len(prices)-2,-1,-1):
            profit = max(profit,maxi-prices[i])
            maxi=max(maxi,prices[i])
        return profit    

        
