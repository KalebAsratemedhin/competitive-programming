# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ors = {}
        prev_max = float('-inf')
        n = len(nums)

        def backtrack(i, curr):
            nonlocal prev_max
 
            ors[curr] = ors.get(curr, 0) + 1
            prev_max = max(prev_max, curr)
            if i == n:
                return 

            for j in range(i, n):
                backtrack(j + 1, curr | nums[j])
            
            return 
        backtrack(0, 0)

        return ors[prev_max]
