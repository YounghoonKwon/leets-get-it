class Solution:
    def isMatch(self, s, p):
        T = [
            [False for _ in range(len(s)+1)]
            for _ in range(len(p)+1)
        ]

        T[0][0] = True

        for i in range(1, len(p)+1):
          
            T[i][0] = i > 1 and T[i-2][0] and p[i-1] == '*'

        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):

                if p[i-1] == s[j-1] or p[i-1] == '.':
                    T[i][j] |= T[i-1][j-1]

                elif p[i-1] == '*':

                    T[i][j] |= T[i-1][j]

                  
                    T[i][j] |= i > 1 and T[i-2][j]
 
                    if i > 1 and p[i-2] == s[j-1] or p[i-2] == '.':
                        T[i][j] |= T[i][j-1]

        return T[-1][-1]
