class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = 0
        n = len(cardPoints)
        total = 0
        for i in range(n - k):
            total += cardPoints[i]
        min_score = total
        for i in range(n - k, n):
            total += cardPoints[i]
            total -= cardPoints[left]
            left += 1
            min_score = min(min_score, total)
        return sum(cardPoints) - min_score
        

        
