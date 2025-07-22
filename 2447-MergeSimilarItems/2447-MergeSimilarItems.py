# Last updated: 7/22/2025, 3:26:02 PM
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.sort()
        items2.sort()
        
        first, second = 0, 0
        ret = []

        while first < len(items1) and second < len(items2):
            if items1[first][0] == items2[second][0]:
                ret.append([items1[first][0], items1[first][1] + items2[second][1] ])
                first += 1
                second += 1
            elif items1[first][0] < items2[second][0]:
                ret.append(items1[first])
                first += 1
            else:
                ret.append(items2[second])
                second += 1

        while first < len(items1):
            ret.append(items1[first])
            first += 1
        
        while second < len(items2):
            ret.append(items2[second])
            second += 1

        return ret

            

