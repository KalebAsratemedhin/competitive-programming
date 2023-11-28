class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        n = len(height)
        right = n - 1
        maxima = 0
        while left < right:
            area = min(height[left], height[right]) *(right - left)
            maxima = max(area, maxima)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxima


        