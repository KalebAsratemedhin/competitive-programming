# Last updated: 7/22/2025, 3:25:25 PM
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        def dfs(i, j, load):
            nonlocal robot, factory, m, n

            if i >= m:
                return 0

            if j >= n:
                return float('inf')

            if (i, j, load) in memo:
                return memo[(i, j, load)]

            skip = dfs(i, j + 1, 0)
            take = float('inf')

            if factory[j][1] > load:
                distance = abs(robot[i] - factory[j][0])
                new_load = load + 1
                take = distance + dfs(i + 1, j, new_load)

            memo[(i, j, load)] = min(skip, take)
            return memo[(i, j, load)]

        m, n = len(robot), len(factory)
        memo = dict()
        robot = sorted(robot)
        factory = sorted(factory)

        return dfs(0, 0, 0)

