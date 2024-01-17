class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        hand = {}
        count = 0
        ans = 0
        max_count = 0
        i = 0
        for j in range(n):
            hand[s[j]] = hand.get(s[j], 0) + 1
            count += 1
            max_count = max(max_count, hand[s[j]])
            window_len = j - i + 1
            if window_len - max_count > k:
                hand[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
                

        return ans