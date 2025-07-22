# Last updated: 7/22/2025, 3:26:44 PM
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = [0] * (n + 1)
        score = {}
        for i in range(n):
            if nums[i] == 0:
                zeros[i + 1] += 1
            zeros[i + 1] += zeros[i] 
        count = 0
        highest = 0
        
        for j in range(n, -1, -1):
            if j < n and nums[j] == 1:
                count += 1
            sc = zeros[j] + count
            highest = max(highest, sc)
            if sc in score:
                score[sc].append(j)
            else:
                score[sc] = [j]
            
        return score[highest]

        






