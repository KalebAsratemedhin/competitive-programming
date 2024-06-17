# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c ** (1/2)) 
        while l <= r:
            curr = l ** 2 + r ** 2
            if curr == c:
                return True
            
            elif curr > c:
                r -= 1
            else:
                l += 1
        return False
