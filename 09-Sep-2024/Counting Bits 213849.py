# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        num, j = 1, 0

        for i in range(1, n + 1):
            if i == 2 * num:
                j = 0
                num = i
            ans.append(ans[j] + 1)
            j += 1
            
        return ans

