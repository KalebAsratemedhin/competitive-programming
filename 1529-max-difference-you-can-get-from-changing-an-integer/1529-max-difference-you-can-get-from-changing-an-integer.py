class Solution:
    def maxDiff(self, num: int) -> int:
        def remap(ans, s, target, cand=-1, refrain=-1):
            for d in s:
                if cand == -1 and d != target and d != refrain:
                    cand = d
                if d == cand:
                    ans.append(target)
                else:
                    ans.append(d)
            return int("".join(ans))
        
        word = str(num)
        max_ = remap([], word, '9')

        if word[0] == '1':
            min_ = remap(['1'], word[1:], '0', refrain='1')
        else:
            min_ = remap([], word, '1', word[0])

        return max_ -  min_
            
