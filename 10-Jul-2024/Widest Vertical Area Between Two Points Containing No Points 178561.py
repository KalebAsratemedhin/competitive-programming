# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxDist = 0
        n = len(points)

        for i in range(1, n):
            maxDist = max(maxDist, points[i][0] - points[i - 1][0] )
        return maxDist
