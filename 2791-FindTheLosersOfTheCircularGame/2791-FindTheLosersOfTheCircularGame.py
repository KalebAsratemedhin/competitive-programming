# Last updated: 7/22/2025, 3:24:32 PM
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        arr = [0] * n
        
        curr = 0
        diff = k
        while not arr[curr]:
            arr[curr] = 1
            curr = (curr + diff) % n
            diff += k
            
        
        ans = []
        for i, num in enumerate(arr):
            if not num:
                ans.append(i + 1)
            
        return ans

        
