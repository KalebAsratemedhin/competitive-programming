class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)
        ans = [-1, -1]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == 0 or nums[mid] != nums[mid - 1]):
                ans[0] = mid
                break
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
                ans[1] = mid
                break
            elif target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        return ans
