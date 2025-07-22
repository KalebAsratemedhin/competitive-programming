# Last updated: 7/22/2025, 3:23:01 PM
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        letters = [ord(c) - ord('a') for c in s]
        mod = 10 ** 9 + 7

        @cache
        def dp(a, b, left):
            if left == 0:
                s = 0
                s = s + (1 if a != None else 0)
                s = s + (1 if b != None else 0)
                
                return s

            ans = 0
            if a != None:
                if left >= 26 - a:
                    ans += dp(0, 1, left - (26 - a))
                else:
                    ans += 1
            if b != None:
                if left >= 26 - b:
                    ans += dp(0, 1, left - (26 - b))
                else:
                    ans += 1

            return ans % mod

        ans = 0
        for num in letters:
            res = dp(num, None, t)
            ans += res


        return (ans) % mod