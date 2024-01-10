class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        ans = 0
        for right in range(len(s)):
            if right - left < k:
                if s[right] in vowels:
                    vowel_count += 1
            else:
                if s[right] in vowels:
                    vowel_count += 1
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1
            ans = max(ans, vowel_count)
        return ans
            

