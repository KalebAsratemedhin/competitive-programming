class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        sum = 0
        for j in range(3):
            sum += nums[j]
        minimum_diff = target - sum
        for i in range(n - 1):
            left = i + 1
            right = n - 1            
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum < target - nums[i]:
                    left += 1
                elif two_sum > target - nums[i]:
                    right -= 1
                else:
                    sum = two_sum + nums[i]     
                    minimum_diff =  abs(target - two_sum - nums[i])  
                    break
                if abs(target - two_sum - nums[i]) < minimum_diff:
                    sum = two_sum + nums[i]     
                    minimum_diff =  abs(target - two_sum - nums[i])              

        return sum

                
