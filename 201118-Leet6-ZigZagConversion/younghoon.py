class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        delta = -1
        row = 0
        result = [[] for i in range(numRows)]
        for c in s:
            result[row].append(c)
            if row == 0 or row == numRows - 1:
                delta *= -1
            row += delta
        
        for i in range(numRows):
            result[i] = ''.join(result[i])
        return ''.join(result)
