class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        n = len(s2)
        left = right = 0
        window = {}
        size = 0
        while right < n:
            if s2[right] not in target:
                left += 1 + size
                right += 1
                size = 0
                window = {}
            else:
                window[s2[right]] = window.get(s2[right], 0) + 1
                size += 1
                while window[s2[right]] > target[s2[right]] and left < right:
                    window[s2[left]] -= 1
                    if window[s2[left]] == 0:
                        del window[s2[left]]
                    left += 1
                    size -= 1
                right += 1
            if size == len(s1):
                return True
        return False


