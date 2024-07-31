# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = {}
        i = j = 0
        n = len(fruits)
        ans = 0
        
        while i < n and j < n:
            if fruits[j]  in types:
                types[fruits[j]] = j
                ans = max(ans, j + 1 - i)
                j += 1
            else:
                if len(types) < 2:
                    types[fruits[j]] = j
                    ans = max(ans, j + 1 - i)
                    j += 1
                else:
                    if i == types[fruits[i]]:
                        i = types.pop(fruits[i]) + 1
                    else:
                        i += 1
        return ans