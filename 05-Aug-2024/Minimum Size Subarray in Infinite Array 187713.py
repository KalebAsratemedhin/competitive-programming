# Problem: Minimum Size Subarray in Infinite Array - https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        
        sum_ = sum(nums)

        def findMinSubarray(total, nums):
            temp = nums + nums
            prefix = {0: -1}
            length = float("inf")
            num = 0
            for i in range(len(temp)):
                num += temp[i]
                if num - total in prefix:
                    length = min(length, i - prefix[num - total])
                prefix[num] = i
            return length if length != float("inf") else -1
        if sum_ == target:
            return len(nums)
        elif target < sum_:
            return findMinSubarray(target, nums) 
        else:
            ans = target // sum_
            target %= sum_
            if not target:
                return ans * len(nums)
            temp = findMinSubarray(target, nums)
            
            return temp + ans * len(nums) if temp != -1 else -1
    


        
