# Last updated: 7/22/2025, 3:25:48 PM
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        diff = k - abs(endPos - startPos) 

        if diff % 2 != 0 or diff < 0:
            return 0

        return (factorial(k) // (factorial(k - diff // 2) * factorial(diff // 2))) % (10**9 + 7) 
        
        
