class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = set()
        n = len(cards)
        left = 0
        subarray_length = n + 1
        for right in range(n):
            while cards[right] in seen:
                subarray_length = min(subarray_length, right - left + 1)
                seen.discard(cards[left])
                left += 1
            seen.add(cards[right])
        if subarray_length == n + 1:
            return -1
        return subarray_length