# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        prefix = [0] * len(arr)
        ans = []

        for i in range(len(arr)):
            if i >= 1:
                prefix[i] ^= prefix[i - 1]
                
            prefix[i] ^= arr[i]

        for start, end in queries:

            xor = prefix[end]
            if start >= 1:
                xor ^= prefix[start - 1]
            
            ans.append(xor)

        return ans
