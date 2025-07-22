# Last updated: 7/22/2025, 3:24:29 PM
class Solution:
    def punishmentNumber(self, n: int) -> int:
        

        def can_be_partitioned(square, root, i, prev_sum):

            if i >= len(square):
                if prev_sum == root:
                    return True
                return False
            
            for j in range(i, len(square)):
                curr_part = int(square[i: j + 1])
                prev_sum += curr_part
                if prev_sum > root:
                    return False
                res = can_be_partitioned(square, root, j + 1, prev_sum)

                if res:
                    return True
                prev_sum -= curr_part

            return False


        ans = 0
        for i in range(1, n + 1):
            if can_be_partitioned(str(i * i), i, 0, 0):
                ans += i * i

        return ans

            
            

            
