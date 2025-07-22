# Last updated: 7/22/2025, 3:25:01 PM
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)

        curr_sum = 0
        nums = 0
        for i in range(1, n + 1):
            if i not in banned and curr_sum + i <= maxSum:
                curr_sum += i
                nums += 1
            if curr_sum >= maxSum:
                return nums
        return nums