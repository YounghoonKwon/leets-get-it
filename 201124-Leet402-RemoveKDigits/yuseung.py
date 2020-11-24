class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if '' == num:
            return '0'

        n = len(num)
        stk = []
        
        for ch in num:
            while k > 0 and stk and stk[-1] > ch:
                stk.pop()
                k -= 1
            stk += ch,
        
        while k > 0:
            stk.pop()
            k -= 1
        
        while stk and stk[0] == '0':
            stk.pop(0)
        
        return '0' if not stk else ''.join(stk)
