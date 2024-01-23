class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        arr = [0] * (n + 1)
        ans = 0 
        nums.sort()
        for req in requests:
            arr[req[0]] += 1
            arr[req[1] + 1] -= 1
        for i in range(1, n + 1):
            arr[i] += arr[i - 1]
        arr.sort()
        for i in range(n - 1, -1, -1):
            ans += nums[i] * arr[i + 1]
        return ans % (10 ** 9 + 7)