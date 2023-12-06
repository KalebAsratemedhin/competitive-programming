class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        rem = n % 7
        days = weeks / 2 * (56 + (weeks - 1) * 7)
        for i in range(1, rem + 1):
            days += (i + weeks)
        return int(days)