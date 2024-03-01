class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr = []

        for i in range(1, len(weights)):
            arr.append(weights[i] + weights[i - 1])
        arr.sort()
        minima = 0
        maxima = 0
        for i in range(k - 1):
            minima += arr[i]
        
        for i in range(k - 1):
            maxima += arr[len(arr) - 1 - i]
        return maxima - minima
        