# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def dp(i):
            if i <= 1:
                return 1
                
            ans =  0
            for j in range(1, i):
                ans = max(ans,(i - j) * j, j * dp(i - j))
            return ans
            
        return dp(n)

