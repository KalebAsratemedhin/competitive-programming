# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        two = 2
        three = 2
        five = 4
        arr = [1, 2, 3, 4, 5]

        if n <= len(arr):
            return arr[n - 1]
        
        n -= len(arr) 
        visited = set(arr)

        
        while n:
            by_two = 2 * arr[two]
            by_three = 3 * arr[three]
            by_five = 5 * arr[five]

            while by_two in visited or by_three in visited or by_five in visited:
                if by_two in visited:
                    two += 1
                
                if by_three in visited:
                    three += 1

                if by_five in visited:
                    five += 1

                by_two = 2 * arr[two]
                by_three = 3 * arr[three]
                by_five = 5 * arr[five]

            targ = min(by_two, by_three, by_five)

            if targ == by_two:
                two += 1
            elif targ == by_three:
                three += 1
            elif targ == by_five:
                five += 1

            arr.append(targ)
            visited.add(targ)
            
            n -= 1
        print(arr)
        return arr[-1]
        