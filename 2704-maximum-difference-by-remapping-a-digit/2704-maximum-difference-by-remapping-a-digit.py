class Solution:
    def minMaxDifference(self, num: int) -> int:
        def remap(ans, target):
            cand = -1
            for d in str(num):
                if cand == -1 and d != target:
                    cand = d
                    
                if d == cand:
                    ans.append(target)
                else:
                    ans.append(d)

            return int("".join(ans))        

        return remap([], '9') - remap([], '0')

