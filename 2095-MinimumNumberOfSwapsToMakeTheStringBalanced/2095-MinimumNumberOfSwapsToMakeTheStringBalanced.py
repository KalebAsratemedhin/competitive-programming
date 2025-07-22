# Last updated: 7/22/2025, 3:27:33 PM
class Solution:
    def minSwaps(self, s: str) -> int:

        stack = []
        for bracket in s:
            if stack and stack[-1] == '[' and bracket == ']':
                stack.pop()
            else:
                stack.append(bracket)

        opening = len(stack) // 2
                
        return (opening // 2 + opening % 2)
        

