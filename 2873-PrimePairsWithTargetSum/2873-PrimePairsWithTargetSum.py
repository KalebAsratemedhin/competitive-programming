# Last updated: 7/22/2025, 3:24:19 PM
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        primes = [1] * (n + 1)
        primes[0] = primes[1] = 0
        d = 2
        while d * d <= n:

            if primes[d]:
                m = d * d
                while m <= n:
                    primes[m] = 0
                    m += d

            d += 1

        ans = []
        st = set()

        for i in range(len(primes)):
            if primes[i] == 1:
                st.add(i)
                if n - i in st:
                    ans.append([n - i, i])
        return ans[::-1]
