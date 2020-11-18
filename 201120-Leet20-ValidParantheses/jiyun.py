class Solution(object):
    def isValid(self, s):
        pairs = {'(': ')', '[':']', '{':'}'}
        stack = []
        
        for i in s:
            if i in pairs:
                stack.append(i)
            elif stack and i == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []
            
