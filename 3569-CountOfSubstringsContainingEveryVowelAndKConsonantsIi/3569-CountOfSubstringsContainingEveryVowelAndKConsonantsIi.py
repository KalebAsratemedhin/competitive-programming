# Last updated: 7/22/2025, 3:23:06 PM
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        num_valid_substrings = 0
        start = end = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = {}  
        consonant_count = 0 
        next_consonant = [0] * len(
            word
        )  
        next_consonant_index = len(word)

        for i in range(len(word) - 1, -1, -1):
            next_consonant[i] = next_consonant_index
            if (word[i]) not in vowels:
                next_consonant_index = i

        while end < len(word):
            new_letter = word[end]
            if new_letter in vowels:
                vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
            else:
                consonant_count += 1

            while (
                consonant_count > k
            ):  
                start_letter = word[start]
                if start_letter in vowels:
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1

            while (
                start < len(word)
                and len(vowel_count) == 5
                and consonant_count == k
            ):  
                num_valid_substrings += next_consonant[end] - end
                start_letter = word[start]
                if start_letter in vowels:
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1

            end += 1

        return num_valid_substrings