class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        placeholder = n - 1
        pointer = n - 1
        while pointer >= 0 :
            if nums[pointer] == val:
                nums[pointer], nums[placeholder] = nums[placeholder], nums[pointer]
                placeholder -= 1
            pointer -= 1
        return placeholder + 1
