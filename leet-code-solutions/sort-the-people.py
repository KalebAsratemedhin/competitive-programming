class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        arr = []
        for i in range(n):
            arr.append((heights[i], names[i]))
        arr.sort(reverse = True)
        for i in range(n):
            names[i] = arr[i][1]

        return names
