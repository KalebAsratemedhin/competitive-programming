class Solution:
    def isHappy(self, n: int) -> bool:
        track = set()
        while n > 1:
            sum = 0
            m = n
            while m > 0:
                rem = m % 10
                m = m // 10
                sum += rem * rem
            n = sum
            if n in track:
                return False
            track.add(sum)
        if n == 1:
            return True 

