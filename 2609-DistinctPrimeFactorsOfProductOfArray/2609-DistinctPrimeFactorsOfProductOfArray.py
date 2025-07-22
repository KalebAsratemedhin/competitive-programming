# Last updated: 7/22/2025, 3:25:10 PM
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def factorize(num):
            prime_factors = set()
            d = 2

            while d * d <= num:
                while num % d == 0:
                    num //= d
                    prime_factors.add(d)
                d += 1

            if num > 1:
                prime_factors.add(int(num))

            return len(prime_factors)


        product = 1
        for num in nums:
            product *= num

        return factorize(product)
