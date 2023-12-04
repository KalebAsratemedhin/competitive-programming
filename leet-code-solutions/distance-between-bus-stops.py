class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        i = start
        n = len(distance)
        sum1 = 0
        sum2 = 0
        while i != destination:            
            sum1 += distance[i]
            i = (i + 1) % n
        
        i = destination 
        while i != start:
            sum2 += distance[i]
            i = (i + 1) % n
        return min(sum1, sum2)



        