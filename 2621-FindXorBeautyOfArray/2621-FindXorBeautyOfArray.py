# Last updated: 7/22/2025, 3:25:06 PM
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num
            
        return xor