https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        # def helper(stepCount,target):
        #     if target==0:
        #         return 1
        #     oneCount = 0
        #     twoCount = 0    
        #     if target-1>=0:
        #         oneCount = helper(stepCount+1,target-1)
        #     if target-2>=0:
        #         twoCount = helper(stepCount+1,target-2)
        #     return oneCount+twoCount
        # return helper(0,n)           
        if n==1 or n==2:
            return n
        dp=[-1]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]    

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        n1 = 1
        n2 = 2
        for i in range(3,n+1):
            curr = n1+n2
            n1,n2 = n2,curr

        return n2        

        
