# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []

        for left, right in intervals:
            if heap and heap[0] < left:
                heapq.heappop(heap)
                heapq.heappush(heap, right)

            else:
                heapq.heappush(heap, right)
        
        return len(heap)
