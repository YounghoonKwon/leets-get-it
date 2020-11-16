class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        cycle = numRows * 2 - 2
        result = []
        for row in range(numRows):
            for i in range(row, len(s), cycle):
                result.append(s[i])
                between = i + cycle - row * 2
                if row != 0 and row != numRows-1 and between < len(s):
                    result.append(s[between])
        return ''.join(result)
