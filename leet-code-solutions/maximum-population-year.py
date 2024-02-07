class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = {}
        for l in logs:
            years[l[0]] = years.get(l[0], 0) + 1
            years[l[1]] = years.get(l[1], 0) - 1
        yrs  = list(years.keys())
        yrs.sort()
        sum = 0
        ans = years[yrs[0]]
        ans_year = yrs[0]
        for y in yrs:
            sum += years[y]
            if sum > ans:
                ans_year = y
                ans = sum
        return ans_year
