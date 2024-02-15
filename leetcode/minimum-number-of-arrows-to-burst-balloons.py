class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        end = points[0][1]
        min_end = end
        arrows = 0
        for i in range(1, len(points)):
            if points[i][0] > min_end:
                end = points[i][1]
                min_end = end
                arrows += 1
            elif points[i][0] > end:
                end = points[i][1]
                arrows += 1
            else:
                min_end = min(min_end, points[i][1])


        return  arrows + 1