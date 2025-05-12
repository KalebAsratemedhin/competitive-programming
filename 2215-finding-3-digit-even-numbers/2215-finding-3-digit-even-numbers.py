class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        cnt_ = Counter(digits)

        for i in range(1, 10):
            for j in range(10):
                for k in [0, 2, 4, 6, 8]:
                    lst = [str(i), str(j), str(k)]
                    cnt = Counter(lst)
                    num = int("".join(lst))
                    valid = True
                    for key, val in cnt.items():
                        if cnt[key] > cnt_[int(key)]:
                            valid = False
                    if valid:
                        ans.append(num)
        return ans

