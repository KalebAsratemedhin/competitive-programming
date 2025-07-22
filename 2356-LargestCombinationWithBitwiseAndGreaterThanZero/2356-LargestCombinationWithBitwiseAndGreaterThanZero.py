# Last updated: 7/22/2025, 3:26:21 PM
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [0 for i in range(32)]

        for num in candidates:
            for i in range(32):
                if (1 << i) & num:
                    bits[i] += 1

        
        return max(bits)
