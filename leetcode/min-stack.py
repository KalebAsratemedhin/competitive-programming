class MinStack(object):

    def __init__(self):
        self.__minStack = []
        self.min = 0
        self.mins = []

    def push(self, val):
        if len(self.__minStack) == 0:
            self.min = val
            self.mins.append(val)
        elif val <= self.min:
            self.mins.append(self.min)
            self.min = val

        self.__minStack.append(val)

    def pop(self):
        if self.__minStack[-1] == self.min:
            self.min = self.mins[-1]     
            self.mins.pop()
        return self.__minStack.pop()

    def top(self):
        return self.__minStack[-1]

    def getMin(self):
        return self.min
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()