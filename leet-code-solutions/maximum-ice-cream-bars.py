class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        n = len(costs)
        freq = [0] * n
        while coins > 0 and i < n:
            coins -= costs[i]
            if coins >= 0:
                freq[i] = 1
            i += 1
        count = 0
        for f in freq:
            if f == 1:
                count += 1

        return count

