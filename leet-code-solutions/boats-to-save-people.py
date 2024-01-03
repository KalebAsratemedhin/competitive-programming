class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        least = 0
        largest = len(people) - 1
        boats = 0
        while least <= largest:
            if people[largest] + people[least] <= limit:
                least += 1
            boats += 1
            largest -= 1
        return boats


