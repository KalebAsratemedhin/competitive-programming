# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        seeker, placeholder = 0, 0
        curr = 0

        while seeker < len(chars):
            length = 0
            while seeker < len(chars) and chars[seeker] == chars[curr]:
                length += 1
                seeker += 1
            
            
            if length == 1:
                chars[placeholder] = chars[curr]
                placeholder += 1
                
            else:
                chars[placeholder] = chars[curr]
                placeholder += 1
                for c in str(length):
                    chars[placeholder] = c
                    placeholder += 1

            curr = seeker
        return placeholder
                

            
