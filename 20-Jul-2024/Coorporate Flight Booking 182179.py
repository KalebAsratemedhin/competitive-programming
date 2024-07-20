# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n + 1)

        for start, end, seat in bookings:
            answer[start - 1] += seat
            answer[end] -= seat

        for i in range(1, n):
            answer[i] += answer[i - 1]
            
        answer.pop()
        return answer