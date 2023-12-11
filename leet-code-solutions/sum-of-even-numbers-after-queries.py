class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sum = 0
        for num in nums:
            if num % 2 == 0:
                sum += num
        for q in queries:
            if nums[q[1]] % 2 == 0:
                if q[0] % 2 == 0:
                    nums[q[1]] += q[0]
                    sum += q[0]
                else:
                    sum -= nums[q[1]]
                    nums[q[1]] += q[0]

            elif nums[q[1]] % 2 != 0:
                if q[0] % 2 != 0:
                    sum += nums[q[1]] +  q[0]
                    nums[q[1]] += q[0]
                else:
                    nums[q[1]] += q[0]

            ans.append(sum)
        return ans