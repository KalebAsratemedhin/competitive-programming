class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_len = 0
        for num in nums:
            if max_len >= len(numbers):
                break
            lower = num - 1
            while num in numbers:
                numbers.remove(num)
                num += 1
            while lower in numbers:
                numbers.remove(lower)
                lower -= 1
            max_len =  max(max_len, num - lower - 1)
        return max_len

        
            
            
        