# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1


        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            
            if nums[low] == nums[high]:
                low += 1

            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[high] >= target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            
        return False