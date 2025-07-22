# Last updated: 7/22/2025, 3:25:33 PM
class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        vals = list(freq.values())
        max_, min_ = max(vals), min(vals)

        # min is 1 all others are equal
        prev = None
        min_count = vals.count(min_)
        max_count = vals.count(max_)

        if len(vals) == 1:
            return True

        if min_ == 1:
            if min_count > 1 and len(set(vals)) <= 1:
                return True
                
            if min_count == 1 and len(set(vals)) - 1 <= 1:
                return True
            
        
            

        # all others are equal, max is greater by 1

        
        # if len(set(vals)) <= 2 and :
        #     return True
        if max_ - min_ == 1:
            if max_count > 1 and len(set(vals)) <= 1:
                return True
                
            if max_count == 1 and len(set(vals)) - 1 <= 1:
                return True
        # there is a gap greater than 1 b/n min and max
        # equal freq not 1
        # 

        
        return False