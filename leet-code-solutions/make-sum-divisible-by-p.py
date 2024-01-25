class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        mod_arr = [0] * n 
        total = 0
        for i in range(n) : 
            mod_arr[i] = nums[i] % p 
            total += nums[i] 
            
        target = total % p

        if (target == 0): 
            return 0
        modulos = {} 
        modulos[0] = -1
        curr = 0
        ans = n + 1

        for i in range(n): 
            curr = (curr + nums[i]) % p 
            modulos[curr] = i 
            mod = (curr - target) % p
            if (mod in modulos.keys()): 
                ans = min (ans, i - modulos[mod]) 

        if ans == n + 1 or ans == n: 
            return -1
        return ans