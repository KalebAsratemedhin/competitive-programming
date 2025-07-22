# Last updated: 7/22/2025, 3:23:27 PM
class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = s[0]
        score = 0
        for c in s:
            score += abs(ord(c) - ord(prev))
            prev = c
        return score

