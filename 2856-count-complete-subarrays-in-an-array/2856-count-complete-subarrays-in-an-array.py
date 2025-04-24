class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        window = defaultdict(int)
        distinct = len(set(nums))

        left = 0
        count = 0
        n = len(nums)

        for right in range(n):
            window[nums[right]] += 1
            while len(window) >= distinct :
                count += n - right
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
        
        return count




