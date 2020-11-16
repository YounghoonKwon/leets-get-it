class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        result = ''
        length = len(s)
        iterate = 2 * numRows - 2
        
        ## sol1
        # for i in range(numRows):
        #     for j in range(i, length, iterate):
        #         result += s[j]
        #         if i != 0 and i != numRows - 1 and j + iterate - 2 * i  < length:
        #             result += s[j + iterate - 2 * i]
        # return result
        
        
        ## sol2
        rowNum = 1
        jump = 1
        rows ={}
        for c in s:
            if not rowNum in rows:
                rows[rowNum] = c
            else:
                rows[rowNum] += c
            rowNum += jump
            if rowNum == 1 or rowNum == numRows:
                jump *= -1
            
        return ''.join(rows.values())
