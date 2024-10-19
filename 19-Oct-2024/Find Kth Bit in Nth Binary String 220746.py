# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev = ['0', '0']
        for i in range(2, n + 1):
            curr = [prev[i - 1] + '1']
            for j in prev[i - 1][::-1]:
                if j == '0':
                    curr.append('1')
                else:
                    curr.append('0')
            prev.append(''.join(curr))
        
        return prev[-1][k - 1]





        