# Last updated: 7/22/2025, 3:25:11 PM
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # find window-max-size
        max_size = {
            'a': 0,
            'b': 0,
            'c': 0
        }
        counts = Counter(s)
        window = {}
        size = 0

        for key, val in counts.items():
            max_size[key] = val - k
            if max_size[key] < 0:
                return -1

        if len(counts) < 3 and k > 0:
            return -1

        j = 0
        n = len(s)
        ans = n
        for i in range(n):
            

            # while good grow window
            window[s[i]] = window.get(s[i], 0) + 1
            size += 1

            # while bad shrink window

            while window and window[s[i]] > max_size[s[i]]:
                window[s[j]] -= 1
                size -= 1

                if not window[s[j]]:
                    del window[s[j]]
                j += 1

            
            ans = min(ans, n - size)

        return ans
            



