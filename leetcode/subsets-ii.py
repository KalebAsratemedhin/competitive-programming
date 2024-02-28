class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort()
        def helper(start):
            ans.append(subset.copy())
            for i in range(start, len(nums)):
                if i == start or nums[i] != nums[i - 1]:
                    subset.append(nums[i])
                    helper(i + 1)
                    subset.pop()
        
        helper(0)
        return ans