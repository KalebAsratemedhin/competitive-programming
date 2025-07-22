# Last updated: 7/22/2025, 3:23:28 PM
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 0
        increasing = []
        decreasing = []

        for num in nums:

            if increasing and num <= increasing[-1]:
                increasing = []
            
            if decreasing and num >= decreasing[-1]:
                decreasing = []

            if not increasing or num > increasing[-1]:
                increasing.append(num)
            
            if not decreasing or num < decreasing[-1]:
                decreasing.append(num)

            longest = max(len(increasing), len(decreasing), longest)
        
        return longest
        

