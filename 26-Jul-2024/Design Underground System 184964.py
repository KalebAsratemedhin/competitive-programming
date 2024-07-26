# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.diff = {}
        self.averageTime = {}
        self.freq = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]            

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.diff[(self.check_in[id][0], stationName)] = self.diff.get((self.check_in[id][0], stationName), 0) + t - self.check_in[id][1]
        self.freq[(self.check_in[id][0], stationName)] = self.freq.get((self.check_in[id][0], stationName), 0) + 1

        self.averageTime[(self.check_in[id][0], stationName)] = self.diff[(self.check_in[id][0], stationName)] / self.freq[(self.check_in[id][0], stationName)]
      
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averageTime[(startStation,endStation)]

        



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)