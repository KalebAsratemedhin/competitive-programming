# Last updated: 7/22/2025, 3:27:12 PM
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        maxhpq = [(0, float('inf'))]       
        for start, _, value in events:
            heappush(maxhpq, (-value, start))

        events = sorted(events, key=lambda x: x[1])
        res = 0            
        max_value = 0      

        for _, end, value in events:
            max_value = max(max_value, value)
            while maxhpq and end >= maxhpq[0][1]:
                heappop(maxhpq)

            res = max(res, max_value - maxhpq[0][0])

        return res