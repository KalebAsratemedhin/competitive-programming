# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:

        start.sort()
        low = 0
        high = (start[-1] + d - start[0]) // (len(start) - 1)

        def check(sep):
            arr = [start[0]]
            for i in range(1, len(start)):
                if arr[i - 1] + sep > start[i] + d:
                    return False
                if start[i] <= arr[i - 1] + sep <= start[i] + d:
                    arr.append(arr[i - 1] + sep)
                else:
                    arr.append(start[i])
                    
            return True

        

        while low <= high:
            mid = (low + high) // 2

            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high


