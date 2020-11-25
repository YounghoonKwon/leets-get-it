class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        size = len(num)
        if size == k: return '0'
        stack = []
        for i, n in enumerate(num):
            while stack and k and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)
            if len(stack)==1 and stack[-1] == '0': 
                stack.pop()
            if not k:
                res = ''.join(stack)+num[i+1:]
                return res if res else '0'
        while k:
            stack.pop()
            k-=1
        return ''.join(stack)
