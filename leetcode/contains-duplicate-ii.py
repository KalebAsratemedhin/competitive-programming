class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        right = 0
        n = len(nums)
        dict = set()
        for right in range(n):
            while nums[right] in dict:
                if nums[left] == nums[right]:
                    dict.discard(nums[left])
                    if left < right and abs(right - left) <= k:
                        return True
                left += 1
            
            dict.add(nums[right])
        return False
