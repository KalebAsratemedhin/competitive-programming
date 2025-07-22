# Last updated: 7/22/2025, 3:23:16 PM
class Solution:
    def compressedString(self, word: str) -> str:
        stack = []

        for c in word:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            elif stack and c == stack[-1][0]:
                if stack[-1][1] >= 9:
                    stack.append([c, 1])
                else:
                    stack[-1][1] += 1

        ans = [f'{num}{c}' for c, num in stack]
        return "".join(ans)
                

        