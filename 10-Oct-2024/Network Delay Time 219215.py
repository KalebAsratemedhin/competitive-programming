# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for i in range(n)]
        distances = [float("inf") for i in range(n)]
        distances[k - 1] = 0

        for u, v, w in times:
            graph[u - 1].append((v - 1, w))
        
        heap = [(0, k - 1)]

        while heap:
            d, curr = heapq.heappop(heap)

            for node, time in graph[curr]:
                if distances[curr] + time < distances[node]:
                    distances[node] = distances[curr] + time
                    heapq.heappush(heap, (distances[node], node))

        ans = -float("inf")
        for time in distances:
            if time == float("inf"):
                return -1
            ans = max(ans, time)

        return ans

        


        
        

