Brute Force - Two loops
#TC:O(n2),SC:O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

Optimal
#TC:O(n),SC:O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            t = target-nums[i]
            if t in hm:
                return[i,hm[t]]
            hm[nums[i]]=i    


        
