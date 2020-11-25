Standard solution:

def removeKdigits(self, num: str, k: int) -> str:
        size = len(num)
        if size == k: return '0'
        stack = []
        for n in num:
            while stack and k and stack[-1] > int(n):
                stack.pop()
                k -= 1
            if len(stack) == 1 and stack[-1] == 0:# not leading 0
                stack.pop()
            stack.append(int(n))
        while k:
            stack.pop()
            k -= 1
        return ''.join(map(str,stack))  
