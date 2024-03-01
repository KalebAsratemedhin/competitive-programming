class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        maxima = 0  
        i = 0  
        counts = {'T': 0, 'F': 0}  

        for j in range(n):
            counts[answerKey[j]] += 1

            while min(counts['T'], counts['F']) > k:
                counts[answerKey[i]] -= 1
                i += 1

            maxima = max(maxima, j - i + 1)

        return maxima
                
            