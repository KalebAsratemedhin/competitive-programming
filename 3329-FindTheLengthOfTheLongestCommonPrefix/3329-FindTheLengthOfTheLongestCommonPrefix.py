# Last updated: 7/22/2025, 3:23:35 PM
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        ans = 0

        for num in arr1:
            for d in range(len(str(num))):
                prefixes.add(str(num)[:d + 1])

        for num in arr2:
            for d in range(len(str(num))):
                if str(num)[:d + 1] in prefixes:
                    ans = max(ans, d + 1)
        
        return ans
            
