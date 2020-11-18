class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #edge case
        if len(s) <= 1:
            return s
        
        matrix = [[] for _ in range(numRows)]
        
        pointer = 0
        down = True
        for idx_letter in range(len(s)):
            matrix[pointer].append(s[idx_letter]) 
            if down:
                if pointer >= (numRows-1):
                    down = False
                    pointer -=1
                else:
                    pointer += 1
            else:
                if pointer <= 0:
                    down = True
                    pointer +=1
                else:
                    pointer -=1
        
        result = ''
        for idx_row in range(numRows):
            current = ''.join(matrix[idx_row])
            result += current
        return result
        # PAYPALISHIRING
        # 
        # P   A   H   N
        # A P L S I I G
        # Y   I   R
