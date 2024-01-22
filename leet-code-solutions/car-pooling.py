class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0] * 1000
        n = len(trips)
        sum = 0
        for trip in trips:
            passengers[trip[1] - 1] += trip[0]
            if passengers[trip[1] - 1] > capacity:
                return False
            passengers[trip[2] - 1] -= trip[0]

        for person in passengers:
            sum += person
            if sum > capacity:
                return False
        return True