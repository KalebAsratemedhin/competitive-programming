# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostK(nums, K):
            window = defaultdict(int)
            left = 0
            ans = 0

            for right in range(len(nums)):
                window[nums[right]] += 1

                while len(window) > K:
                    window[nums[left]] -= 1
                    if not window[nums[left]]:
                        del window[nums[left]]
                    left += 1

                ans += (right - left + 1)
            return ans

        return atmostK(nums, k) - atmostK(nums, k - 1)
        
