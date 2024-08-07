# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        below_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if num == 0:
            return "Zero"

        def chunks(n):
            if n < 20:
                return below_twenty[n]
            elif n < 100:
                return tens[n // 10] + ('' if n % 10 == 0 else ' ' + below_twenty[n % 10])
            else:
                return below_twenty[n // 100] + ' Hundred' + ('' if n % 100 == 0 else ' ' + chunks(n % 100))
            
        
        billions, num = divmod(num, 1000000000)
        millions, num = divmod(num, 1000000)
        thousands, num = divmod(num, 1000)
        
        ans = []
        if billions:
            ans.append(chunks(billions) + ' Billion')
        if millions:
            ans.append(chunks(millions) + ' Million')
        if thousands:
            ans.append(chunks(thousands) + ' Thousand')
        if num:
            ans.append(chunks(num))

        return ' '.join(ans)
        


