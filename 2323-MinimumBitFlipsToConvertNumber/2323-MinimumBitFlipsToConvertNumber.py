# Last updated: 7/22/2025, 3:26:28 PM
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = (start ^ goal)
        return xor.bit_count()