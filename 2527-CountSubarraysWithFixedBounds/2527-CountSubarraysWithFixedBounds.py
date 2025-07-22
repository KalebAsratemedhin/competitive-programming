# Last updated: 7/22/2025, 3:25:35 PM
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        near_min = near_max = -1
        start = count = 0
        
        for index, num in enumerate(nums):
            if num == minK:  
                near_min = index
            if num == maxK: 
                near_max = index
            if not (minK <= num <= maxK):
                start = index + 1
                near_min = near_max = -1

            if near_max != -1 and near_min != -1:
                count += min(near_max, near_min) - start + 1


        return count


