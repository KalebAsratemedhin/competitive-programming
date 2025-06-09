class Solution(object):
    def findKthNumber(self, n, k):
        curr = 1
        k -= 1

        while k > 0:
            step = self.count_steps(n, curr)
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1

        return curr

    def count_steps(self, n, prefix1):
        prefix2 = prefix1 + 1
        steps = 0
        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
            
        return steps