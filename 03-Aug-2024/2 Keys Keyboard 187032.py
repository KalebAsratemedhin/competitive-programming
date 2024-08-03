# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        val = 1
        clip = 0
        ops = 0

        while val < n:
            if clip:

                if clip < val and n - val >=  val and (n - val) % val == 0:
                    clip = val
                    ops += 1
                else:
                    val += clip
                    ops += 1
            else:
                clip = val
                ops += 1
       


        return ops

