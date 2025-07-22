# Last updated: 7/22/2025, 3:25:21 PM
class Solution:
    def pivotInteger(self, n: int) -> int:
        sum = 0
        left = 0
        for num in range(1,n + 1):
            sum += num
        for i in range(1, n + 1):
            left += i
            if left == sum:
                return i
            sum -= i
        return -1