# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        @cache
        def dp(index, mask):
            if index == n:
                return 0
            
            ans = float("inf")
            for i in range(n):
                if not mask & (1 << i):
                    ans = min(ans, dp(index + 1, mask | (1 << i)) + (nums1[index] ^ nums2[i]))
            
            return ans

        return dp(0, 0)