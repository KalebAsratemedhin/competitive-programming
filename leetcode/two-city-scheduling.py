class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        sortedCosts = sorted(costs, key = lambda x: x[1] - x[0])
        total = 0

        for i in range(n):
            if i < n // 2:
                total += sortedCosts[i][1]
            else:
                total += sortedCosts[i][0]


        return total

        

