# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        left = right = total = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        base = 1

        for i in range(n):
            if word[i] in vowels:
                break
            left += 1
            base += 1

        if left < n:
            total += base

        for right in range(left + 1, n):

            if word[right] not in vowels:
                total += base
            else:
                total += base + (right + 1)
                base += (right + 1)
                left = right
               
        return total
