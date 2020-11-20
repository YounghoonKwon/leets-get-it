class Solution:
    def pair(self, start:str, end: str):
        if start=='(' and end==')':
            return True
        elif start=='[' and end==']':
            return True
        elif start=='{' and end=='}':
            return True
        else:
            return False
        
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            if s[i] in ('(', '[', '{'):
                stack.append(s[i])
                
            if s[i] in (')', ']', '}'):
                if len(stack)==0 or self.pair(stack[-1], s[i])==False:
                    return False
                else:
                    stack.pop()
                    
        if len(stack)==0:
            return True
        else:
            return False
