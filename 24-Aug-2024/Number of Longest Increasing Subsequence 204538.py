# Problem: Number of Longest Increasing Subsequence - https://leetcode.com/problems/number-of-longest-increasing-subsequence/


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        @cache
        def count_lis(start, prev):
            if start == len(nums):
                return 0, 1  

            pick, pick_count = 0, 0
            if nums[start] > prev:
                pick, pick_count = count_lis(start + 1, nums[start])
                pick += 1
            no_pick, no_pick_count = count_lis(start + 1, prev)

            if pick  > no_pick:
                return pick , pick_count
            elif pick  == no_pick:
                return pick , pick_count + no_pick_count
            else:
                return no_pick, no_pick_count

        return count_lis(0, float('-inf'))[1]