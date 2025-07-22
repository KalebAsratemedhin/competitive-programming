# Last updated: 7/22/2025, 3:25:46 PM
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        freed = list(range(n))
        heapify(freed)
        heap = []
        rooms = [0] * n
        for start, end in sorted(meetings):
            while heap and heap[0][0] <= start:
                a, room_number = heappop(heap)
                heappush(freed, room_number)
            if freed:
                room_number = heappop(freed)
                heappush(heap, (end, room_number))
            else:
                end_time, room_number = heappop(heap)
                heappush(heap, (end_time + end - start, room_number))
            rooms[room_number] += 1

        max_ = 0
        for i, room in enumerate(rooms):
            if rooms[i] > rooms[max_]:
                max_ = i
        return max_