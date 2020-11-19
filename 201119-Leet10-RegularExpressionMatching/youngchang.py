class Solution(object):
    def isMatch(self, text, pattern):
        T = len(text)
        P = len(pattern)
        
        @lru_cache(None)
        def recur(i, j):
            if j == P:
                return i == T
            
            first_match = i < T and pattern[j] in (text[i], '.')
            if j + 1 < P and pattern[j + 1] == '*':
                res = recur(i, j + 2) or first_match and recur(i + 1, j)
            else:
                res = first_match and recur(i + 1, j + 1)
            
            return res
        
        return recur(0, 0)