class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        ans = ""
        while i >= 0:
            if s[i] == '#':
                ans += chr(96 + int(s[i - 2 : i]))
                i -= 3
            else:
                ans += chr(96 + int(s[i]))
                i -= 1
        return ans[::-1]