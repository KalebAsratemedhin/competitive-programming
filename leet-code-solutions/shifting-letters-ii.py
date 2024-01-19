class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * n
        ans = ""
        for shift in shifts:
            if shift[2] == 0:
                arr[shift[0]] -= 1
                if shift[1] + 1 < n:
                    arr[shift[1] + 1] += 1
            elif shift[2] == 1:
                arr[shift[0]] += 1
                if shift[1] + 1 < n:
                    arr[shift[1] + 1] -= 1
        for i in range(1, n):
            arr[i] += arr[i - 1]
        for i in range(n):
            arr[i] += ord(s[i]) - ord('a')
            arr[i] %= 26 
            arr[i] += ord('a')
            ans += chr(arr[i])
        return ans
