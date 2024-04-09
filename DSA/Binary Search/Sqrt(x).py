https://leetcode.com/problems/sqrtx/description/
https://www.youtube.com/watch?v=zdMhGxRWutQ

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        left = 1
        right = x//2 + 1
        res = 0
        while left<=right:
            mid = (left+right)//2
            if mid*mid == x:
                return mid
            elif mid*mid >x:
                right = mid-1
            else:
                left = mid+1
                res = mid
        return res            

            


        
