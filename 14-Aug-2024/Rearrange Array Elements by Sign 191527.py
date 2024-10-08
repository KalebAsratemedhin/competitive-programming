# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives = []
        positives = []
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                negatives.append(nums[i])
            else:
                positives.append(nums[i])
                
        for i in range(n // 2):
            nums[2 * i] = positives[i]
            nums[2 * i + 1] = negatives[i]
            
        return nums