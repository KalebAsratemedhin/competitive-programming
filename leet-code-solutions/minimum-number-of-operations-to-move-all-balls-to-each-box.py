class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        operations = []
        ones = []
        n = len(boxes)
        for i in range(n):
            if boxes[i] == '1':
                ones.append(i)
        for i in range(n):
            ops = 0
            for j in ones:
                ops += abs(j - i)
            operations.append(ops)
        return operations



