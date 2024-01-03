class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right = 1
        left = 0
        n = len(nums)
        while right < n:
            if nums[right] != nums[left]:
                nums[left + 1], nums[right] = nums[right], nums[left + 1]
                left += 1
            right += 1
        return left + 1

