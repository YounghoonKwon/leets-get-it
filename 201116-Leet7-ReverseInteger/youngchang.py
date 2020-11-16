class Solution:
    def reverse(self, x: int) -> int:
        lo = -2 ** 31
        hi = 2 ** 31 - 1
        
        x = str(x)
        sign = 1
        if x[0] == '-':
            x = x[1:]
            sign = -1
        
        answer = int(x[::-1]) * sign
        return answer if lo <= answer <= hi else 0