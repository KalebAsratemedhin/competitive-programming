# Last updated: 7/22/2025, 3:25:05 PM
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def gcd(num1, num2):
            if num2 == 0:
                return num1

            return gcd(num2, num1 % num2)
        
        
        lcm = int(divisor1 * divisor2 / gcd(divisor1, divisor2))

        
        low = 1
        high = divisor1 * uniqueCnt1 + divisor2 * uniqueCnt2

        while low < high:
            mid = (low + high) // 2

            indiv1 = mid - (mid // divisor1)
            indiv2 = mid - (mid // divisor2)
            indiv_lcm = mid - (mid // lcm) 
            if indiv1 >= uniqueCnt1 and indiv2 >= uniqueCnt2 and indiv_lcm >= uniqueCnt1 + uniqueCnt2:
                high = mid
            else:
                low = mid + 1

       

        return low


        
        


             

