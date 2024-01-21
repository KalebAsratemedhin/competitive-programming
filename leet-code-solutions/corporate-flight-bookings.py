class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * n
        for booking in bookings:
            answer[booking[0] - 1] += booking[2]
            if booking[1] < n:
                answer[booking[1]] -= booking[2]

        for i in range(n):
            if i >= 1:
                answer[i] += answer[i - 1]
        return answer