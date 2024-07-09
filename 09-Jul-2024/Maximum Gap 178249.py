# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        min_nums, n = min(nums), len(nums)
        range_nums = max(nums) - min_nums
        buckets = [[] for i in range(n)]

        if not range_nums:
            return range_nums

        for num in nums:
            ind = int((num - min_nums) * (n - 1) / range_nums)
            buckets[ind].append(num)
        
        index = 0
        for arr in buckets:
            if arr:
                buckets[index] = (min(arr), max(arr))
                index += 1


        maxGap = 0
        for i in range(index - 1):
            maxGap = max(buckets[i + 1][0] - buckets[i][1], maxGap)

        return maxGap

