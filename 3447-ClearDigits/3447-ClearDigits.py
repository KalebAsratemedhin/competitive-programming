# Last updated: 7/22/2025, 3:23:17 PM
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i].isalpha():
                stack.append(s[i])
            elif stack:
                stack.pop()
        
        return "".join(stack)

