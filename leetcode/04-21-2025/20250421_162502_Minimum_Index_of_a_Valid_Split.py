class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        total = Counter(nums)
        running = {}
        n = len(nums)

        for i, num in enumerate(nums):
            total[num] -= 1
            running[num] = running.get(num, 0) + 1

            if running[num] > (i + 1) // 2 and total[num] > (n - i - 1) // 2:
                return i
        return -1

