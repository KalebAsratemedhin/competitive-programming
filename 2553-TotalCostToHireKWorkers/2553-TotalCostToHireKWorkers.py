# Last updated: 7/22/2025, 3:25:26 PM
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap1, heap2, heap = [], [], []
        left, right = candidates - 1, len(costs) - candidates
        total_cost = 0

        if right <= left:
            for i, num in enumerate(costs):
                heapq.heappush(heap, (num, i))
        
        else:
            for i, num in enumerate(costs):
                if i <= left:
                    heapq.heappush(heap1, (num, i))
                elif i >= right:
                    heapq.heappush(heap2, (num, i))
            
        while k and left < right:
            if len(heap1) < candidates:
                heapq.heappush(heap1, (costs[left], left))
            if len(heap2) < candidates:
                heapq.heappush(heap2, (costs[right], right))

            cost1, i = heapq.heappop(heap1)
            cost2, j = heapq.heappop(heap2)
            k -= 1

            if cost1 < cost2 or (cost1 == cost2 and  i < j):
                total_cost += cost1
                left += 1
                heapq.heappush(heap2, (cost2, j))
            else:
                total_cost += cost2
                right -= 1
                heapq.heappush(heap1, (cost1, i))


        if heap1 or heap2:
            heap = heap1 + heap2
            heapq.heapify(heap)


        while k and heap:
            cos = heapq.heappop(heap)[0]
            total_cost += cos
            k -= 1
        return total_cost