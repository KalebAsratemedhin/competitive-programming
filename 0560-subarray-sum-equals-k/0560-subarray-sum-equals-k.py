class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        sums = defaultdict(int)
        sums[0] = 1

        for num in nums:
            prefix += num
            count += sums[prefix - k]
            sums[prefix] += 1

        return count