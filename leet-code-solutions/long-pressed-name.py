class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        first = 0
        second = 0
        n = len(name)
        m = len(typed)
        typed_freq = 0
        name_freq = 0
        while first < n and second < m:
            if first < n - 1 and name[first] == name[first + 1]:
                name_freq += 1
                first += 1
            if second < m - 1 and typed[second] == typed[second + 1]:
                typed_freq += 1
                second += 1
            else:
                if typed[second] != name[first] or name_freq > typed_freq:
                    return False
                first +=1 
                second += 1
                name_freq = typed_freq = 0
        
        if first < n or second < m:
            return False
        return True

