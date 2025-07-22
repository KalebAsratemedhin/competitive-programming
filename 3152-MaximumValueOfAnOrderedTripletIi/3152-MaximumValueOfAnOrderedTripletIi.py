# Last updated: 7/22/2025, 3:24:02 PM
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans, a, ab = 0, 0, 0
        for num in nums:
            ans = max(ans, ab * num)
            ab = max(ab, a - num)
            a = max(a, num)
        return ans