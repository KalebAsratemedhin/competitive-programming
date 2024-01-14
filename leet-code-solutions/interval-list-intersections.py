class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        first = 0
        second = 0
        ans = []
        while first < n and second < m:
            first_start, first_end = firstList[first][0], firstList[first][1]
            second_start, second_end = secondList[second][0], secondList[second][1]
            if first_start <= second_end and first_end >= second_start:
                ans.append([max(firstList[first][0], secondList[second][0]),
                 min(firstList[first][1], secondList[second][1])])
            if first_end <= second_end:
                first += 1
            else:
                second += 1
        return ans

