class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        previous = 0
        n = len(s)
        for i in range(n - 1, -1, -1):
            if dict[s[i]] >= previous:
                num += dict[s[i]]
                previous = dict[s[i]]
            else:
                num -= dict[s[i]]
        return num

        