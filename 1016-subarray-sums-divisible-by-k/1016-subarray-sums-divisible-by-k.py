class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        rems = defaultdict(int)
        rems[0] = 1

        for num in nums:
            prefix += num
            count += rems[prefix % k]
            rems[prefix % k] += 1

        return count

