class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1] or len(s) < 2:
            return s

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i,i+1), expand(i, i+2), key=len)
        return result
            
            
                
                
