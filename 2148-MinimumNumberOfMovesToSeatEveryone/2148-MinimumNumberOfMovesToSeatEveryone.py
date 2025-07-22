# Last updated: 7/22/2025, 3:27:18 PM
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort() 
        students.sort()
        moves = 0
        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])
        
        return moves
