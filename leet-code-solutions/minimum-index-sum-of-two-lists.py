class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        max_sum = len(list1) + len(list2) - 2
        output = []
        hashmap = {}
        for index, value in enumerate(list1):
            hashmap[value] = index
        for i in range(len(list2)):
            if list2[i] in hashmap:
                if (hashmap[list2[i]] + i) == max_sum:
                    max_sum = hashmap[list2[i]] + i 
                    output.append(list2[i])
                if (hashmap[list2[i]] + i) < max_sum:
                    output = []
                    max_sum = hashmap[list2[i]] + i 
                    output.append(list2[i])
                
        return output