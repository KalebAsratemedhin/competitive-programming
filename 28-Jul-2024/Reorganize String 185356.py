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
            if not ans or ans[-1] != char:
                ans.append(char)
                freq += 1
                if freq:
                    heapq.heappush(heap, (freq, char))
                continue

            if not heap:
                break

            freq2, char2 = heapq.heappop(heap)
            
            ans.append(char2)
            freq2 += 1
            if freq2:
                heapq.heappush(heap, (freq2, char2))

            heapq.heappush(heap, (freq, char))
             
        ans = "".join(ans)
        if len(ans) < len(s):
            return ""
        
            
        return ans 



