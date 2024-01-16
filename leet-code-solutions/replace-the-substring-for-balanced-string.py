class Solution:
    def balancedString(self, s: str) -> int:
        substring = len(s)
        dict = Counter(s)
        n = len(s)
        replacement = {}
        for key, value in dict.items():
            if dict[key] > n // 4:
                replacement[key] = dict[key] - (n // 4)
        
        window = len(replacement)
        if len(replacement) == 0:
            return 0
        start = 0
        for i in range(n):
            if s[i] in replacement:
                replacement[s[i]] -= 1
                if replacement[s[i]] == 0:
                    window -=1
            while window == 0:
                substring = min(substring, i - start + 1)
                if s[start] in replacement:
                    replacement[s[start]] += 1
                    if replacement[s[start]] == 1:
                        window += 1
                start += 1
                
        
        return substring
        