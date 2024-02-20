class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(b, p):
            if p <= 0:
                return 1
            if p == 1:
                return b
            ans = power(b, (p // 2))
            return ans * ans * (b ** (p % 2)) % (10 ** 9 + 7)
        evens = (n // 2) + (n % 2)
        odds = n - evens
        ans = power(5, evens) *  power(4, odds)
        return ans % (10 ** 9 + 7)