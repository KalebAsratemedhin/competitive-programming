class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        def helper():
            if len(arr) == len(nums):
                ans.append(arr.copy())
                return 
            for i in range(len(nums)):
                if nums[i] != 11:
                    arr.append(nums[i])
                    temp = nums[i]
                    nums[i] = 11
                    helper()
                    nums[i] = temp
                    arr.pop()
                    
        helper()
        return ans
            