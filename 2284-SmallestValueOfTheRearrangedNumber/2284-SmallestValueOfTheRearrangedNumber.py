# Last updated: 7/22/2025, 3:26:37 PM
class Solution:
    def smallestNumber(self, num: int) -> int:
        s = [c for c in str(abs(num))]
        s.sort()
        zero_cutoff = 0
        for c in s:
            if c == '0':
                zero_cutoff += 1
            else:
                break
        if num >= 0:
            ans = s[zero_cutoff: zero_cutoff + 1] + s[:zero_cutoff] + s[zero_cutoff + 1:]
            ans = int("".join(ans))
        else:
            ans = s[::-1]
            ans = -1 * int("".join(ans))
        return ans
