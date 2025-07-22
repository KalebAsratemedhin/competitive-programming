# Last updated: 7/22/2025, 3:25:43 PM
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for num in range(1, 2 * n + 1):
            if num % 2 == 0 and num % n == 0:
                return num
                
