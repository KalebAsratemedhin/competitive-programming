# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        alpha = Counter(s)
        
        for key, val in alpha.items():
            heapq.heappush(heap, (-val, key))

        ans = []
        for i in range(len(s)):
            freq, char = heapq.heappop(heap)
            heap2 = []

            while heap and ans and ans[-1] == char:
                heapq.heappush(heap2, (freq, char))
                freq, char = heapq.heappop(heap)

            if ans and ans[-1] == char:
                return ""
                
            if not ans or ans[-1] != char:
                ans.append(char)
                freq += 1
                
            if freq:
                heapq.heappush(heap, (freq, char))
                
            heap += heap2
            heapq.heapify(heap)
            heap2 = []

            
        return "".join(ans)



