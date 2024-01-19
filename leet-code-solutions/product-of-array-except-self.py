class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_left = nums.copy()
        product_right = nums.copy()
        for i in range(n):
            if i == 0:
                continue
            else:
                product_left[i] *= product_left[i - 1]
                product_right[n - 1 - i] *= product_right[n - i]
        ans = []
        for i in range(n):
            if i - 1 < 0:
                ans.append(product_right[i + 1])
            elif i + 1 >= n:
                ans.append(product_left[i - 1])
            else:
                ans.append(product_left[i - 1] * product_right[i + 1])

        return ans