# Last updated: 7/22/2025, 3:26:34 PM
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_difference = Counter(s) - Counter(t)
        t_difference = Counter(t) - Counter(s)
        return (s_difference.total() + t_difference.total())