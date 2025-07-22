# Last updated: 7/22/2025, 3:26:43 PM
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        @cache
        def dp(ind):
            if ind >= n:
                return 0

            return max(questions[ind][0] + dp(ind + questions[ind][1] + 1), dp(ind + 1))
        return dp(0)
