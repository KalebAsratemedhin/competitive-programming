# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(isBought, i):
            
            if isBought and i < len(prices):
                return max(prices[i] + dp(False, i + 2), dp(isBought, i + 1))
            
            if i >= len(prices) - 1:
                return 0 

            return max(- prices[i] +  dp(True, i + 1), dp(isBought, i + 1))


        return dp(False, 0)

        