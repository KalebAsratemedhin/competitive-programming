class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        prefix = [0 for i in range(len(nums))]

        for l, r in queries:
            prefix[l] += 1
            if r + 1 < len(nums):
                prefix[r + 1] -= 1  
        
        for i in range(len(nums)):
            if i > 0:
                prefix[i] += prefix[i - 1]
            if prefix[i] < nums[i]:
                return False
                
        return True
