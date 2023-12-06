class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        left = []
        right = []
        equal = []
        for i in range(n):
            if nums[i] < pivot:
                left.append(nums[i])
            elif nums[i] > pivot:
                right.append(nums[i])
            else:
                equal.append(nums[i])
        return left + equal + right