# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        freq = 0
        for num in nums:
            if num == 1:
                freq += 1
                ans = max(ans, freq)
            else:
                freq = 0
            

        return ans


