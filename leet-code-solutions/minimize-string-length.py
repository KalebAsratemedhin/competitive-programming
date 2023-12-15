class Solution:
    def minimizedStringLength(self, s: str) -> int:
        unique = set()
        for i in range(len(s)):
            if s[i] not in unique:
                unique.add(s[i])
        return len(unique)

