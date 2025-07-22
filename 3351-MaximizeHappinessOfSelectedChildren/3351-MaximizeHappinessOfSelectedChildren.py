# Last updated: 7/22/2025, 3:23:31 PM
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        i, total, penalty = 0, 0, 0

        while i < len(happiness) and k > 0:
            if happiness[i] - penalty < 0:
                return total
                
            total += happiness[i] - penalty
            i += 1
            penalty += 1
            k -= 1
        return total

