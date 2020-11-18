class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        row_dic = {i:'' for i in range(numRows)}
        row = 0
        desc_flag = 0
        for i in s:
            row_dic[row] += i
            if desc_flag:
                row-=1
            else:
                row+=1
            if row==numRows:
                row-=2
                desc_flag = 1
            if row==-1:
                row+=2
                desc_flag = 0
        answer = ''
        for row in range(numRows):
            answer += row_dic[row]
        return answer