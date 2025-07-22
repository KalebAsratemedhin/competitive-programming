# Last updated: 7/22/2025, 3:27:16 PM
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = (len(rolls) + n) * mean
        target_sum = total - sum(rolls)

        minima, rem = divmod(target_sum, n)

        if minima <= 0:
            return []

        if minima + rem <= 6:
            return [minima for i in range(n - 1)] + [minima + rem]
        elif minima + 1 <= 6:
            return [minima for i in range(n - rem)] + [minima + 1 for j in range(rem)]

