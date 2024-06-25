# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        right, left, count, cost, ans = 0, 0, 0, 0, 0
        costs = {}

        for right in range(n):
            costs[right] = abs(ord(s[right]) - ord(t[right]))
            cost += costs[right]
            count += 1
            if cost <= maxCost:
                ans = max(ans, count)
            while cost > maxCost and left < right + 1:
                cost -= costs[left]
                left += 1
                count -= 1
        return ans
            