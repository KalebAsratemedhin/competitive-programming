# Last updated: 7/22/2025, 3:24:42 PM
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # prepare sieve with size of the max number
        # up to sqrt(max_number), eliminate multiples of numbers
        # primes will be left in the table
        # for every number in nums, subtract the biggest prime smaller than it and such that the difference is greater than the previous if any
        # if no such prime, return False
        # return True
        max_num = max(nums)
        seive = [True for i in range(max_num + 1)]
        m = int(sqrt(max_num)) 
        seive[0] = False
        seive[1] = False

        for i in range(2, m + 1):
            if seive[i]:
                curr = 2 * i
                while curr <= max_num:
                    seive[curr] = False
                    curr += i

        prev = []
        for num in nums:
            is_reduced = False
            for i in range(num - 1, -1, -1):
                if seive[i]:
                    if not prev:
                        prev.append(num - i)
                        is_reduced = True
                        break
                    elif prev[-1] < num - i:
                        prev.append(num - i)
                        is_reduced = True
                        break

            if not is_reduced and (not prev or prev[-1] < num):
                prev.append(num)

        return False if len(prev) < len(nums) else True

        
      



      


