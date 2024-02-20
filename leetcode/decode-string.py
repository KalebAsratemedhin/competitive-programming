class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s, index = 0):
            decoded = []
            freq = 0

            while index < len(s):
                if s[index] == "[":
                    string, index = decode(s, index + 1)
                    decoded.append(string * freq)
                    freq = 0
                elif s[index] == "]":
                    return "".join(decoded), index
                elif s[index].isnumeric():
                    freq = freq * 10 + int(s[index])
                else:
                    decoded.append(s[index])
                index += 1
            return "".join(decoded), index

        decoded, index = decode(s)
        return decoded
