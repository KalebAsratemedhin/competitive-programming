class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        nums = {}
        ans = [] 
        for i in range(len(arr1)):
            if arr1[i] in nums:
                nums[arr1[i]] += 1
            else:
                nums[arr1[i]] = 1 

        for j in range(len(arr2)):
            ans += [arr2[j] for i in range (nums[arr2[j]])]
            del nums[arr2[j]]
        temp = list(nums.keys())
        temp.sort()
        for k in temp:
            ans += [k for i in range (nums[k])]
        return ans

