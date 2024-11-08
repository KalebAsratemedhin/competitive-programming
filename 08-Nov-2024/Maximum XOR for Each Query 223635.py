# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix = 0
        ans = []
        for num in nums:
            prefix ^= num
            ans.append(prefix ^ ((2 ** maximumBit) - 1))
        
        return ans[::-1]