class Solution(object):
    def isMatch(self, s, p):
        ## using 're' module
        
        # match = re.search(p, s)
        # if not match:
        #     return match
        # else:
        #     return re.search(p, s).group() == s
        
        ## also can be
        # if re.compile('^'+p+'$').match(s):
        #     return True
        # else:
        #     return False
        
        ## use recursion
        if not p:
            return not s
        firstMatch = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or firstMatch and self.isMatch(s[1:], p)
        else:
            return firstMatch and self.isMatch(s[1:], p[1:])
