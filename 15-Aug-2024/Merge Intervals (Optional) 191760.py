# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        left = 0
        end = intervals[left][1]

        for right in range(1, len(intervals)):
            if intervals[right][0] > end:
                ans.append([intervals[left][0], end])
                
                left = right
                end = intervals[right][1]

            else:
                if intervals[right][1] > end:
                    end = intervals[right][1]

        if left < len(intervals):
            ans.append([intervals[left][0], end])
        return ans
