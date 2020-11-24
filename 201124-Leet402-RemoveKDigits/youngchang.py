class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return '0'
        if len([i for i in num if i != '0']) == k: return '0'
        stack = []
        for n in num:
            if k == 0:
                stack.append(n)
            elif not stack:
                stack.append(n)
            elif stack[-1] <= n:
                stack.append(n)
            else:
                while stack[-1] > n:
                    stack.pop()
                    k -= 1
                    if not stack or k == 0: break
                stack.append(n)
                if len(stack) == 1 and stack[0] == '0':
                    stack.pop()
        while k:
            stack.pop()
            k -= 1
        while stack and stack[0] == '0':
            stack.pop(0)
        return ''.join(stack)