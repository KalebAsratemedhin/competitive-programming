# Last updated: 7/22/2025, 3:25:12 PM
class Solution:
    def smallestValue(self, n: int) -> int:
        def sumPrimes(num):
            d = 2
            count = 0
            while d * d <= num:
                while num % d == 0:
                    count += d
                    num //= d
                d += 1
            if num > 1:
                count += num
            return count
        
        while True:
            count = sumPrimes(n)
            if count == n:
                return count
            n = count
