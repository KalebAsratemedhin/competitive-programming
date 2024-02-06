class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_pt = len(s) - 1
        t_pt = len(t) - 1
        s_back = 0
        t_back = 0

        while s_pt >= 0 and t_pt >= 0:
            if s[s_pt] == t[t_pt] and s[s_pt] != "#":
                s_pt -= 1
                t_pt -= 1
            elif s[s_pt] != "#" and t[t_pt] != "#" and s[s_pt] != t[t_pt]:
                return False
            else:
                while s[s_pt] == "#" and s_pt >= 0:
                    s_back += 1
                    s_pt -= 1
                while t[t_pt] == "#" and t_pt >= 0:
                    t_back += 1
                    t_pt -= 1
                while s_back > 0 and s_pt >= 0:
                    if s[s_pt] == "#":
                        s_back += 1
                    else: 
                        s_back -= 1
                    s_pt -= 1
                while t_back > 0 and t_pt >= 0:
                    if t[t_pt] == "#":
                        t_back += 1
                    else: 
                        t_back -= 1
                    t_pt -= 1
        extras = 0
        while t_pt >= 0:
            if t[t_pt] == "#":
                t_back += 1
            else: 
                if t_back > 0:
                    t_back -= 1
                else:
                    extras += 1
            t_pt -= 1
        while s_pt >= 0:
            if s[s_pt] == "#":
                s_back += 1
            else: 
                if s_back > 0:
                    s_back -= 1
                else:
                    extras += 1
            s_pt -= 1
        
        if t_pt < 0 and s_pt < 0 and extras == 0:
            return True
        return False
                    

