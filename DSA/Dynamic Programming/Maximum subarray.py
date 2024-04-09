https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        max_here = 0
        for i in range(0,len(nums)):
            max_here += nums[i]
            if maxSum < max_here:
                maxSum = max_here
            if max_here < 0:
                max_here = 0

                   

        return maxSum    
