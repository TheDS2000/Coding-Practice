https://leetcode.com/problems/counting-bits/description/

import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return[0]
        elif n==1:
            return [0,1]

        ans = [0]*(n+1)
        for i in range(1,n+1):
            ans[i]=ans[i//2]+i%2
        return ans    



        
