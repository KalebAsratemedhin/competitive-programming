class Solution(object):
    def twoSum(self, nums, target):
        found=False
        ans=[]
        for i in range(0,len(nums)):
            if found:
                break
            for j in range(0,len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    ans.append(i)
                    ans.append(j)
                    found=True
        return ans