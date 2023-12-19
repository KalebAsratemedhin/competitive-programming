class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        start = 0
        i = 0
        while i < n:
            if i + k <= n:
                ans += s[i: i + k ][:: -1]
                ans += s[i + k: i + 2 * k]
            else:
                ans += s[i: ][::-1]
            i += 2 * k

        return ans

