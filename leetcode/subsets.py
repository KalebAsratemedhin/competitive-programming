class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def helper(start):
            if start > len(nums):
                return
            ans.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                helper(i + 1)
                subset.pop()
        helper(0)
        return ans
            
