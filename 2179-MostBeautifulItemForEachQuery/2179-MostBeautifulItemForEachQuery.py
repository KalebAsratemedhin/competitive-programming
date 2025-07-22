# Last updated: 7/22/2025, 3:27:05 PM
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        heap = []

        for price, beauty in items:
            heapq.heappush(heap, (-1 * beauty, -1 * price))
        
        arr = [(num, ind) for ind, num in enumerate(queries)]
        ans = [0] * len(arr)
        arr.sort(reverse=True)

        for num, ind in arr:

            while heap and -1 * heap[0][1] > num:
                heapq.heappop(heap)
            
            if heap and -1 * heap[0][1] <= num:
                ans[ind] = -1 * heap[0][0] 

        return ans


