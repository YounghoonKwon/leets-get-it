from functools import lru_cache
class Solution:
    def isMatch(self, s, p) -> bool:
        if len(p.replace('*', '')) > len(s): return False
        N = len(s)
        pN = len(p)
        @lru_cache(maxsize = None)
        def recur(sp, pp):
            if sp == N:
                if all(True if i == '*' else False for i in p[pp:]):
                    return True
                else:
                    return False
            if pp == pN:
                if sp != N:
                    return False
                else:
                    return True
                
            answer = False
            if s[sp] == p[pp]:
                answer = max(answer, recur(sp + 1, pp + 1))
            elif p[pp] == '?':
                answer = max(answer, recur(sp + 1, pp + 1))
            elif p[pp] == '*':
                for i in range(sp, N + 1):
                    answer = max(answer, recur(i, pp + 1))
                    if answer: break
            return answer
        return recur(0, 0)  