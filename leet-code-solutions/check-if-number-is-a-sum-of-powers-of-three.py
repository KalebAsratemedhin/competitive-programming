class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        divider = n
        while divider >= 3:
            rem = divider % 3
            divider = divider // 3
            if rem > 1:
                return False
            if divider == 1:
                return True
        if divider > 1:
            return False
        else:
            return True



        


            
