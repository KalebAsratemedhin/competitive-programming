# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        vowels = {'a': 16, 'e': 8, 'i': 4, 'o': 2, 'u': 1}
        num = 0
        pref = {0: -1}
        ans = 0

        for i in range(len(s)):
            if s[i] in vowels:
                num ^= vowels[s[i]]
                
            if num not in pref:
                pref[num] = i
            else:
                ans = max(ans, i - pref[num])


        return ans
