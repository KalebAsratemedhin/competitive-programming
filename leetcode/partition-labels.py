class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        n = len(s)
        map = {}
        start = 0
        for i in range(n):
            map[s[i]] = i

        while start < n:
            end = map[s[start]]
            i = start + 1
            while i < end:
                end = max(end, map[s[i]])
                i += 1
            ans.append(end - start + 1)
            start = end + 1
           
        return ans


        


