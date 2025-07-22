# Last updated: 7/22/2025, 3:23:39 PM
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        @cache
        def dp(index, isEven):
            if index == len(nums):
                return 0 if isEven == 1 else -float("inf")


            no_xor = nums[index] + dp(index + 1, isEven)

            with_xor = (nums[index] ^ k) + dp(index + 1, isEven ^ 1)

            return max(no_xor, with_xor)

        return dp(0, 1)

            

