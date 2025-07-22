# Last updated: 7/22/2025, 3:23:14 PM
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count = 0
        arr = colors + colors
        left = right = 0 

        while left < len(colors) and right < len(arr):
            if right - left >= 1:
                if arr[right] == arr[right - 1]:
                    left = right
            
            if right - left + 1 == k:
                left += 1
                count += 1

                
            right += 1

        return count