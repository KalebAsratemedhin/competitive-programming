# Last updated: 7/22/2025, 3:23:23 PM
class Solution:
    def isValid(self, word: str) -> bool:
        has_vowel = has_consonant = False
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for c in word:
            if not c.isalnum():
                return False
            if c.isalpha():
                if c in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant and len(word) >= 3