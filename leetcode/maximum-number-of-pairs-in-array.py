class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dict = Counter(nums)
        answer = [0,0]

        for key, value in dict.items():
            answer[0] += value // 2
            answer[1] += value % 2
        return answer