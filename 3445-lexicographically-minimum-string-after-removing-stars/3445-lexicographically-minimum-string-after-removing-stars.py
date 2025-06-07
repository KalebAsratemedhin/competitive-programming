class Solution:
    def clearStars(self, s: str) -> str:
        heap = []

        for ind, char in enumerate(s):
            if char != '*':
                heapq.heappush(heap, [ord(char), -ind])
                continue
            if heap:
                heapq.heappop(heap)

        heap.sort(key=lambda x: -x[1])
        return "".join([chr(letter) for letter, ind in heap])

        


            