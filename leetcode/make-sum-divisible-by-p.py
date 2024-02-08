class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        target = sum(nums) % p

        if (target == 0): 
            return 0

        modulos = {0: -1} 
        curr = 0
        ans = n + 1

        for i in range(n): 
            curr = (curr + nums[i]) % p 
            modulos[curr] = i 
            mod =  (curr - target) % p
            if mod in modulos: 
                ans = min (ans, i - modulos[mod]) 

        if ans == n + 1 or ans == n: 
            return -1
        return ans