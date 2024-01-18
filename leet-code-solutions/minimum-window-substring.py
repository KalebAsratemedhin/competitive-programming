class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        start = 0
        dict_t = Counter(t)
        ans = [0, m]
        window = {}
        disjoint = True
        for i in range(m):
            if s[i] in dict_t:
                window[s[i]] = window.get(s[i], 0) + 1
            if len(window) == len(dict_t):
                substring = True
                while substring and start < m:
                    if len(window) != len(dict_t):
                        break
                    for key, value in dict_t.items():
                        if window[key] < dict_t[key]:
                            substring = False
                            break
                    if not substring:
                        break
                    if i - start < ans[1] - ans[0] :
                        disjoint = False
                        ans = [start, i]
                    if s[start] in window :
                        window[s[start]] -= 1
                        if window[s[start]] == 0:
                            del window[s[start]]
                    
                    
                    start += 1

                
        if disjoint:
            return ""
        return s[ans[0]: ans[1] + 1]
                    
                        






        