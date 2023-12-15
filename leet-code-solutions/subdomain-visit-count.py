class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq = {}
        for cp in cpdomains:
            pair = cp.split()
            freq[pair[1]] = freq.get(pair[1], 0) + int(pair[0])
            for i in range(len(pair[1])):
                if pair[1][i] == '.':
                    freq[pair[1][i + 1:]] = freq.get(pair[1][i + 1:], 0) + int(pair[0])
            
        ans = []
        for key, value in freq.items():
            ans.append(f"{value} {key}")
        return ans