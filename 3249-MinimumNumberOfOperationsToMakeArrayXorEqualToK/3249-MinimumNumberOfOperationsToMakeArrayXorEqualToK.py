# Last updated: 7/22/2025, 3:23:43 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curr = 0
        for num in nums:
            curr ^= num
        
        return (curr ^ k).bit_count()