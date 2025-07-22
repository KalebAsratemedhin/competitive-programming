# Last updated: 7/22/2025, 3:26:49 PM
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        same = 0

        ans = 0
        for key, val in cnt.items():
            if key == key[::-1]:
                tmp = cnt[key]
                if cnt[key] & 1 and same == 0:
                    same += 1
                    ans += 1
                ans += cnt[key] - (cnt[key] & 1)
                
            else:
                ans += min(cnt[key], cnt[key[::-1]])
        
        return ans * 2
            
                
