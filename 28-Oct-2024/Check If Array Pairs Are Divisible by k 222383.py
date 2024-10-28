# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rems = { j : 0 for j in range(k)}

        for x in arr:
            rem = ((x % k))
            rems[rem] += 1
        
        for i in range(1, k):
            if rems[i] != rems[k - i]:
                return False

        if rems[0] % 2:
            return False    

        return True
        
        
