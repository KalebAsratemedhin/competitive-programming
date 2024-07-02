# Problem: Walking Robot Simulation II - https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.direction = "East"
        self.pos = 0
        self.m = height + width - 2

    def step(self, num: int) -> None:
        self.pos += num
        self.pos %=  2 * self.m
        
        if self.pos > self.m + self.width:
            self.direction = "South"
        elif self.pos > self.m:
            self.direction = "West"
        elif self.pos > self.width:
            self.direction = "North"
        elif not self.pos:
            self.direction = "South"
        else:
            self.direction = "East"

            
    def getPos(self) -> List[int]:
        if self.pos > self.m + self.width:
            return [0, self.height - self.pos + self.m + self.width]

        elif self.pos > self.m:
            return [self.width - self.pos + self.m, self.height]

        elif self.pos > self.width:
            return [self.width, self.pos - self.width]

        else:
            return [self.pos, 0]
    def getDir(self) -> str:
        return self.direction
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()