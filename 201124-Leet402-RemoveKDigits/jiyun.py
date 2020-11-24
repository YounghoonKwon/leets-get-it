class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        if k:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or "0"
