class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for par in s:
            if par == '(' or par == '{' or par == '[':
                stack.append(par)
                continue
            if stack:
                opening = stack.pop()
                if (par == ')' and opening == '(') or (par == '}' and opening == '{') or (par == ']' and opening == '['):
                    continue
                return False
            return False
        if stack:
            return False
        return True
            
