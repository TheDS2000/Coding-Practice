https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]

        prevRow = [1]
        for i in range(1,rowIndex+1):
            currRow = [1]*(i+1)
            for j in range(1,i):
                currRow[j]=prevRow[j-1]+prevRow[j]
            prevRow = currRow
        return prevRow          
        
