# Last updated: 7/22/2025, 3:25:51 PM
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
