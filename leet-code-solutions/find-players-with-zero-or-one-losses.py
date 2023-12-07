class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = {}
        for match in matches:
            if match[0] not in losers:
                losers[match[0]] = 0
            losers[match[1]] = losers.get(match[1], 0) + 1
        arr = [[], []]
        for key in losers:
            if losers[key] == 0:
                arr[0].append(key)
            if losers[key] == 1:
              arr[1].append(key)
        arr[0].sort()
        arr[1].sort()
        return arr
