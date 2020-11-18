class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = ""
        if len(s) <= 1:
            return s
        
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(long) >= j-i:
                    continue
                elif s[i:j] == s[i:j][::-1]:
                    long = s[i:j]

        return long
