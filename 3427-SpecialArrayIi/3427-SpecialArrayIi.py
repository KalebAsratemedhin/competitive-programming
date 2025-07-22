# Last updated: 7/22/2025, 3:23:22 PM
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)

        defiants = []
        for i in range(1, len(nums)):
            if (nums[i] % 2 == nums[i - 1] % 2): 
                defiants.append(i)

        
        def has_defiant(defiants, l, r):
            low, high = 0, len(defiants) - 1
            while low <= high:
                mid = (low + high) // 2
                if defiants[mid] < l:
                    low = mid + 1
                elif defiants[mid] > r:
                    high = mid - 1
                else:
                    return True  
            return False

        for i, (l, r) in enumerate(queries):
            ans[i] = not has_defiant(defiants, l + 1, r)

        return ans
