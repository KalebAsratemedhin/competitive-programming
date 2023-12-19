class ATM:

    def __init__(self):
        self.cash = [[20, 0], [50, 0], [100, 0], [200, 0], [500, 0]]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.cash[i][1] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        for i in range(4, -1, -1):
            num = amount // self.cash[i][0]
            if num == 0 or self.cash[i][1] == 0:
                continue
            if self.cash[i][1] >= num:
                amount -= num * self.cash[i][0]
                ans[i] += num
            elif self.cash[i][1] < num:
                amount -= self.cash[i][1] * self.cash[i][0]
                ans[i] += self.cash[i][1]
        if amount != 0:
            return [-1]
        for i in range(5):
            self.cash[i][1] -= ans[i]
            
        return ans
        
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)