# Last updated: 7/22/2025, 3:25:52 PM
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [nums[0]]
        answer = [0] * len(queries)
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        for j in range(len(queries)):
            for i in range(len(prefix)):
                if prefix[i] <= queries[j]:
                    answer[j] += 1
                else:
                    break


        return answer