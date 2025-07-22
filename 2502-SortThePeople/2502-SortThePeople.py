# Last updated: 7/22/2025, 3:25:40 PM
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        arr = [(heights[i], names[i]) for i in range(len(names))]

        arr.sort(reverse = True)
        for i in range(n):
            names[i] = arr[i][1]

        return names