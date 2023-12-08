class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict = {}
        output = []
        for string in paths:
            temp = string.split(" ")
            pre = temp.pop(0)
            for word in temp:
                temp2 = word.split("(")
                value = pre + '/' + temp2[0]
                key = temp2[1].strip(')')
                if dict.get(key):
                    dict[key].append(value)
                else:
                    dict.update({key : [value]})
        for key in dict.keys():
            if len(dict[key]) > 1:
                output.append(dict[key])
        return output