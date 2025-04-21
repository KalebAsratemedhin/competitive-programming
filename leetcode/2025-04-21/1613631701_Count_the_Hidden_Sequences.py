class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_pref = 0
        max_pref = 0
        current = 0
        
        for diff in differences:
            current += diff
            min_pref = min(min_pref, current)
            max_pref = max(max_pref, current)
        
        min_x = lower - min_pref
        max_x = upper - max_pref

        return max(0, max_x - min_x + 1)
