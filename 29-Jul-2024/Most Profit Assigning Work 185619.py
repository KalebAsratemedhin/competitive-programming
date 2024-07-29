# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr = [(profit[i], difficulty[i]) for i in range(len(difficulty))]
        arr.sort(reverse = True)
        total_profit = 0
         
        for ability in worker:
            for prof, diff in arr:
                
                if ability >= diff:
                    total_profit += prof
                    break
                    
        return total_profit
