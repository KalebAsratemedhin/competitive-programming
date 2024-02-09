class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        ans = 0
        penalty = n 
        for i in range(n):
            if customers[i] == "Y":
                penalty += 1
        min = penalty
        for i in range(n):
            if customers[i] == "Y":
                penalty -= 1  
                if  penalty < min :
                    min = penalty
                    ans = i + 1
            else:
                penalty += 1
        return ans