# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        water = capacity

        for index, plant in enumerate(plants):
            steps += 1
            if water < plant:
                steps += 2 * index
                water = capacity
            water -= plant
        return steps