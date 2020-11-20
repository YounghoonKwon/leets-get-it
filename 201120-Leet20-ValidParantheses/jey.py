class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for ch in s :
            if ch == '(' or ch == '{' or ch == '[' :
                l.append(ch)
            else :
                if len(l) == 0 :
                    return False
                elif ch == ')' :
                    if l.pop() != '(' :
                        return False
                elif ch == '}' :
                    if l.pop() != '{' :
                        return False
                elif ch == ']' :
                    if l.pop() != '[' :
                        return False

        return len(l) == 0
