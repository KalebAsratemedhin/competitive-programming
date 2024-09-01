# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for i in range(len(strs)):
            key = str(sorted(strs[i]))
            if key in res:
                res[key].append(strs[i])
            else:
                res[key] = [strs[i]]
        
        return [values for values in res.values()]

        