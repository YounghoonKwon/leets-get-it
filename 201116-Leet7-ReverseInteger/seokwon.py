class Solution:
    def reverse(self, x: int) -> int:
        M = []
        temp = ''
        b = str(x).strip('0')
        if (x == 0) or (x > 2**31 - 1) or (x < -(2**31)):
            return 0
        else:
            for i in b:
                if i.isdigit():
                    M.append(i)
                else:
                    temp = i
            M.append(temp)
            M.reverse()
            dash = ''
            a = dash.join(M)
            if (int(a) > 2**31 - 1) or (int(a) < -(2**31)):
                return 0
            return a

        
