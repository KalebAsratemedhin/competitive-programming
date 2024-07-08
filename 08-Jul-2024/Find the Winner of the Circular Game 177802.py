# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        table = [i for i in range(1, n + 1)]
        j = 0
        removed = 0
        for i in range(n):
            m = k
            while m > 0 and removed < n:
                if table[j % n] != -1:
                    m -= 1
            
                if m == 0 and n - removed > 1:
                    table[j % n] = -1
                    removed += 1

                j += 1

        return [table[i] for i in range(n) if table[i] != -1][0]

        