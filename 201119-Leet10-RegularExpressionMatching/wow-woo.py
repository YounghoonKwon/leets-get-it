class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        st_s = 0
        st_p = 0
        dp = {}
        
        return Solution.recur(st_s, st_p, s, p, dp)

    
    @staticmethod
    def recur(st_s, st_p, s, p, dp):
        if st_p == len(p):
            print('end point', st_s==len(s))
            return st_s == len(s)
        if (st_s, st_p) in dp:
            return dp[st_s, st_p]
        curr_match = True if (st_s < len(s) and p[st_p] in ['.', s[st_s]]) else False
        if st_p <= len(p) - 2 and p[st_p + 1] == '*':
            branch1 = curr_match and Solution.recur(st_s + 1, st_p, s, p, dp) 
            branch2 = Solution.recur(st_s, st_p + 2, s, p, dp)
            print('bran1', branch1)
            print('branch2', branch2)
            print('dp1', dp)
            dp[st_s, st_p] = branch1 or branch2
            print('dp2', dp)
        else:
            dp[st_s, st_p] = curr_match and Solution.recur(st_s + 1, st_p + 1, s, p, dp)
        print('tip of this branch')
        return dp[st_s, st_p]
