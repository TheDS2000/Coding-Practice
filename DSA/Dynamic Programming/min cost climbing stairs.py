class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost
        for i in range(2,len(cost)):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        n = len(cost)
        return min(dp[n-1],dp[n-2])    

https://leetcode.com/problems/min-cost-climbing-stairs/solutions/476388/4-ways-or-Step-by-step-from-Recursion-greater-top-down-DP-greater-bottom-up-DP-greater-fine-tuning/
