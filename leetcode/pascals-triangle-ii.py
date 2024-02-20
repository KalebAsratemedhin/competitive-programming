class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(index):
            if index == 0:
                return [1]
            if index == 1:
                return [1, 1]
            row = pascal(index - 1)
            arr = [1]
            for i in range(1, len(row)):
                arr.append(row[i] + row[i - 1])
            arr.append(1)
            return arr
        return pascal(rowIndex)

