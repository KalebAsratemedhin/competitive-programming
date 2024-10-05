# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window = {}
        left = 0

        for right in range(len(s2)):

            char = s2[right]

            if char in target:
                
                while char in window and window[char] >= target[char]:
                    window[s2[left]] -= 1

                    left += 1

                if char not in window or window[char] < target[char]:
                    window[char] = window.get(char, 0) + 1


                if len(window) == len(target):
                    is_match = True
                    for key, val in window.items():
                        if target[key] != val:
                            is_match = False
                    
                    if is_match:
                        return True

            else:
                left = right + 1
                window = {}


            

        return False


