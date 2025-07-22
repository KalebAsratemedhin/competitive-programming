# Last updated: 7/22/2025, 3:26:01 PM
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        all_pairs = len(nums) * (len(nums) - 1) // 2
        seq_offset = {}

        # Every good pair is part of an increasing sequence. 
        # Each sequence is charachterized by its offset. nums[i] - i = nums[j] - j
        # Exclude the good pairs from all possible pairs and you will have the bad pairs.
        for index, num in enumerate(nums):
            seq_offset[num - index] = seq_offset.get(num - index, 0) + 1
        
        for offset, freq in seq_offset.items():
            all_pairs -= freq * (freq - 1) // 2
        
        return all_pairs

