# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        curr = target
        steps = 0

        while curr > startValue:
            if curr % 2:
                curr += 1
            else:
                curr //= 2
            steps += 1

        
        if curr < startValue:
            steps += startValue - curr
        
        return steps
