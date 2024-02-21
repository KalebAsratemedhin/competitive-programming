class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        depth = 0
        right_max = height[j]
        left_max = height[i]
        while i < j:
            if height[i] <= height[j]:
                i += 1
                if height[i] > left_max:
                    left_max = height[i]
                else: 
                    depth += (left_max - height[i] )
            if height[j] < height[i]:
                j -= 1
                if height[j] > right_max:
                    right_max = height[j]
                else:
                    depth += (right_max - height[j])
        return depth