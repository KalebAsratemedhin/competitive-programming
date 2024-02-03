class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = "aeiou"
        right = len(s) - 1
        for left in range(len(s)):
            if s[left].lower() in vowels:
                while right > left and s[right].lower() not in vowels:
                    right -= 1
                if right <= left:
                    break
                elif s[right].lower() in vowels:
                    s[right], s[left] = s[left], s[right]
                    right -= 1
        
        return "".join(s)