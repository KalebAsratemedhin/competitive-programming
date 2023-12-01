class Solution:
    def fact(self, num):
        if num == 1:
            return num
        return num * self.fact(num - 1)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        count = Counter(nums)
        for k in list( count.keys()):
            if count[k] > 2:
                pairs += self.fact(count[k]) // (self.fact(count[k] - 2) * 2)
            elif count[k]== 2:
                pairs += 1
        return pairs

                



