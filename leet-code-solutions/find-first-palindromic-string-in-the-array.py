class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            right = len(word) - 1
            left = 0
            isPalindrome = True
            while left < right:
                if word[right] == word[left]:
                    right -= 1
                    left += 1
                else:
                    isPalindrome = False
                    break
            if isPalindrome:
                return word
        return ""

        