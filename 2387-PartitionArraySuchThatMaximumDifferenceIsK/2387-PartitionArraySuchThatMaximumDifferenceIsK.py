# Last updated: 7/22/2025, 3:26:18 PM
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, curr = [], [nums[0]]

        for i in range(1, len(nums)):
            if curr and nums[i] - curr[0] <= k:
                curr.append(nums[i])
            else:
                ans.append(curr)
                curr = [nums[i]]
        
        if curr:
            ans.append(curr)

        return len(ans)
