class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams = []
        p_dict = {}
        s_dict = {}
        if len(s) < len(p):
            return []
        for i in range(len(p)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            p_dict[p[i]] = p_dict.get(p[i], 0) + 1

        if s_dict == p_dict:
            anagrams.append(0)
        for j in range(i + 1, len(s)):
            s_dict[s[j - len(p)]] -= 1
            s_dict[s[j]] = s_dict.get(s[j], 0) + 1
            if s_dict[s[j - len(p)]] == 0:
                del s_dict[s[j - len(p)]] 
            if s_dict == p_dict:
                anagrams.append(j - len(p) + 1)
        
        return anagrams
        