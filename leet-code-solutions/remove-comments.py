class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        source_code = ".".join(source) + "."
        clear = False
        new_code = ""
        while not clear:
            inline = source_code.find('//')
            block = source_code.find('/*')
            if block == -1 and  inline == -1:
                clear = True
            else:   
                if block != -1:
                    if block < inline or inline == -1:
                        closing = source_code.find('*/', block + 2, len(source_code))
                        source_code = source_code[:block] + source_code[closing + 2:]
                if inline != -1:
                    if inline < block or block == -1:
                        closing = source_code.find('.', inline + 2, len(source_code))
                        source_code = source_code[:inline] + source_code[closing:]

        ans = source_code.split('.')
        return [i for i in ans if i]
