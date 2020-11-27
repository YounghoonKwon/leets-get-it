class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if not (i, j) in memo:
                if j == len(p): ans = i == len(s)
                else:
                    firstMatch = i < len(s) and p[j] in {s[i], '?', '*'}
                    if p[j] == '*':
                        ans = dp(i, j + 1) or firstMatch and dp(i + 1, j)
                    else:
                        ans = firstMatch and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)
