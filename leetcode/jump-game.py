class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        d = 0
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] >= d:
                d = 0
            d += 1
        if d > 1:
            return False
        return True