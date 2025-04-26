class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_bad = -1
        min_pointer = -1
        max_pointer = -1
        count = 0

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                min_pointer = -1
                max_pointer = -1
                last_bad = i
            if nums[i] == minK:
                min_pointer = i
            if nums[i] == maxK:
                max_pointer = i
            
            if min_pointer != -1 and max_pointer != -1:
                count += min(min_pointer, max_pointer) - last_bad

        return count
                