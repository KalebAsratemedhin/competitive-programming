# Last updated: 7/22/2025, 3:26:23 PM
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        prev = num[0]
        good_num = -1
        count = 0
        for s in num:
            if s == prev:
                count += 1
            else:
                prev= s
                count = 1
            if count >= 3:
                good_num = max(good_num, int(prev))
        if good_num == -1:
            return ""
        return str(good_num) * 3
