# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        d = 2
        first = [1]
        second = [n]
        
        while d * d <= n:
            
            if n % d == 0:
                first.append(d)
                if d != n // d:
                    second.append(n // d)
            d += 1

        ans = first + second[::-1]

        if k > len(ans):
            return -1
        return ans[k - 1]