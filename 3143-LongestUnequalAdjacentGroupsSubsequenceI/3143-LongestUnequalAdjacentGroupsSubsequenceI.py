# Last updated: 7/22/2025, 3:24:05 PM
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []

        for ind, word in enumerate(words):
            if ans and ans[-1][1] == groups[ind]:
                continue
            ans.append((word, groups[ind]))

        
            
           
        return [word for word, group in ans]
           

