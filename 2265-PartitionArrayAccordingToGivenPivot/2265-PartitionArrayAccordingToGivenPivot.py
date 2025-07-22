# Last updated: 7/22/2025, 3:26:42 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [0] * len(nums)
        left, right = 0, len(nums) - 1

        for i in range(len(nums)):
            if nums[i] < pivot:
                ans[left]= nums[i]
                left += 1
            if nums[n - 1 - i] > pivot:
                ans[right] = nums[n - 1 - i]
                right -= 1
            
        for i in range(left, right + 1):
            ans[i] = pivot

        return ans