class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        salary.sort()
        n = len(salary)
        for i in range(1, n - 1):
            sum += salary[i]
        return sum / (n - 2)