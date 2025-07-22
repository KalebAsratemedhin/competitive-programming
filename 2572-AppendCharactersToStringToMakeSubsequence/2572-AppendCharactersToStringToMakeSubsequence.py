# Last updated: 7/22/2025, 3:25:20 PM
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        other = 0

        for pointer in range(len(s)):
            if other < len(t) and s[pointer] == t[other]:
                other += 1
        
        return len(t) - other
            