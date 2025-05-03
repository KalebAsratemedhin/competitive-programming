class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        prev = {tops[0], bottoms[0]}
        n = len(tops)

        for i in range(n):
            intersection = prev.intersection({tops[i], bottoms[i]})
            prev = intersection

            if not intersection:
                return -1
        
        ans = float("inf")

        for num in prev:
            ans = min(ans, n - tops.count(num))
            ans = min(ans, n - bottoms.count(num))

        return ans

       