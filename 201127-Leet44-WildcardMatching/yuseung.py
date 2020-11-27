    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j-1].isalpha() or p[j-1] == '?':
                dp[0][j] = False
            else:
                dp[0][j] = dp[0][j-1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1].isalpha():
                    dp[i][j] = (p[j-1] == s[i-1]) and dp[i-1][j-1]
                elif p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[m][n]
