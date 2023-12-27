class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        dist = 0
        n = len(points)
        for i in range(1, n):
            dist = max(dist, points[i][0] - points[i - 1][0] )
        return dist
