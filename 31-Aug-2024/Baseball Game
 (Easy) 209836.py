# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0

        for op in operations:
            if op == "C":
                sum -= stack.pop()
                continue
                
            if op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

            sum += stack[-1]
            
        return sum