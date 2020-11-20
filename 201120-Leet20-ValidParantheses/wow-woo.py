class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            #Opening parentheses
            if s[i] in ['[', '(', '{']:
                stack.append(s[i])
            #Closing parentheses
            elif s[i] in [']',')','}']:
                #absence means order is NOT valid or Not match
                if len(stack) == 0:
                    return False
                #Bring latest item from stack
                last =stack.pop()
                
                #Concatenate to simply comapre
                current = last + s[i]
                if current not in ['[]', '{}', '()']:
                    return False
            else:
                continue
                
        # string is not formed pairs
        if len(stack) != 0:
            return False
        return True       
