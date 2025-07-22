# Last updated: 7/22/2025, 3:24:14 PM
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # 2 2 5
        # 1 2 3
        freq = defaultdict(int)
        prefix = []
        cnt = 0
        count = 0

        freq[0] = 1

        for num in nums:
            if num % modulo == k:
                cnt += 1
            prefix.append(cnt)
        
        for num in prefix:
            count += freq[(num % modulo - k) % modulo]
            freq[num % modulo] += 1
        
        return count


