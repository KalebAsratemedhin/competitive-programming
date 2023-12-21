class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[-1] += 1
        next_digit = 0
        for i in range(n - 1, -1, -1):
            next_digit = digits[i] // 10
            digit = digits[i] % 10
            digits[i] = digit
            if i - 1 >= 0:
                digits[i - 1] += next_digit
                next_digit = 0
            
        if next_digit != 0:
            return [next_digit] + digits
        return digits
