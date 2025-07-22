# Last updated: 7/22/2025, 3:26:51 PM
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 1
        prev = 1
        n = len(prices)

        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                prev += 1
            else:
                prev = 1
            count += prev

        return count

