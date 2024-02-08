class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        i = j = 0
        l = len(set(nums))
        hand = {}
        count = 0
        while j < n:
            hand[nums[j]] = hand.get(nums[j], 0) + 1
            while l == len(hand):
                hand[nums[i]] -= 1                    
                if hand[nums[i]] == 0:
                    del hand[nums[i]]
                i += 1
                count += n - j 
            j += 1
        return count