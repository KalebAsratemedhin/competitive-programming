# Last updated: 7/22/2025, 3:27:11 PM
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        freq = 0
        prev_max = float('-inf')
        n = len(nums)

        def backtrack(i, curr):
            nonlocal prev_max, freq
 
            if curr > prev_max:
                prev_max = curr
                freq = 1
            elif curr == prev_max:
                freq += 1
            
            if i == n:
                return 

            for j in range(i, n):
                backtrack(j + 1, curr | nums[j])
            
            return 
        backtrack(0, 0)

        return freq
