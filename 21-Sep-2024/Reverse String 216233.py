# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        def reverse(s, right, left = 0):
            if left >= right:
                return
                
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

            reverse(s, right, left)

        reverse(s, n - 1)

        
        
