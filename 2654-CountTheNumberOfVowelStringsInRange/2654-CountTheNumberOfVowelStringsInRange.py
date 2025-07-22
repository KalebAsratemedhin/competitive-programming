# Last updated: 7/22/2025, 3:24:58 PM
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = [0] * (len(words) + 1)
        vowels = {'a','e','i','o','u'}

        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count[i + 1] += 1
            count[i + 1] += count[i] 
        return count[right + 1] - count[left]
