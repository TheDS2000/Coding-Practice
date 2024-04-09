https://leetcode.com/problems/search-insert-position/description/

https://www.youtube.com/watch?v=K-RYzDZkzCI
#O(logn)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        mid = 0
        while left<=right:
            mid = (left+right)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                left =mid+1
            else:
                right=mid-1
        return left              

        
