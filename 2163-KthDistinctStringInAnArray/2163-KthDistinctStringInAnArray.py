# Last updated: 7/22/2025, 3:27:13 PM
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        uniques = Counter(arr)
        i = 0
        for key, value in uniques.items():
            if value == 1:
                i += 1
                if i == k:
                    return key
       
        return ""