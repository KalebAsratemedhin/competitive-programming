# Last updated: 7/22/2025, 3:24:36 PM
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_bank = set(dictionary)

        @cache
        def dp(start, end):
            if end >= len(s):
                return end - start
            
            if s[start: end + 1] in word_bank:
                return min(dp(end + 1, end + 1), dp(start, end + 1))
            
            return min(end - start + 1 + dp(end + 1, end + 1), dp(start, end + 1))

        return dp(0, 0)

            

