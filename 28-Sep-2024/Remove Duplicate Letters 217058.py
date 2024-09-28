# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        used = set()

        for i in range(len(s)):
            if s[i] in used:
                count[s[i]] -= 1
                continue

            while stack and ord(s[i]) < ord(stack[-1]) and count[stack[-1]] > 0:   
                used.discard(stack.pop())

            stack.append(s[i])
            used.add(s[i])
            count[s[i]] -= 1

        return ''.join(stack)
      