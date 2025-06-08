class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(num) for num in range(1, n + 1)]
        nums.sort()
        return [int(num) for num in nums]

