# Last updated: 7/22/2025, 3:24:40 PM
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        numbers = {}

        for i in range(len(nums)):
            if nums[i] in numbers:
                numbers[nums[i]].append(i)
            else:
                numbers[nums[i]] = [i]

        values = numbers.values()
        answer = [0] * len(nums)
        for v in values:
            prefix = []
            sum = 0
            for i in range(len(v)):
                sum += v[i]
                prefix.append(sum)
                
            n = len(v)
            for i in range(n):
                sums = 0
                if i > 0:
                    sums += (i * v[i]) - prefix[i - 1] 
                if i < n - 1:
                    sums += prefix[-1] - prefix[i] - (n - i - 1) * v[i]
                answer[v[i]] = sums
        return answer