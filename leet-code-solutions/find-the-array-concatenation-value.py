class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat_value = 0
        first = 0
        last = len(nums) - 1

        while first < last:
            exp = len(str(nums[last]))
            concat_value += nums[first] * 10 ** exp
            concat_value += nums[last]
            first += 1
            last -= 1
        if first == last:
            concat_value += nums[first]
        return concat_value













