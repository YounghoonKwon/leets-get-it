class Solution:
    def longestPalindrome(self, s: str) -> str:
        #edge case
        if len(s) == 1:
            return s
        
        d={}
        left = 0
        size = 0
        lgs = 0
        result = s[0]
        for left in range(len(s)):
            for right in range(len(s)-1 , left, -1):
                current = s[left:right+1]
                check = isPalindrome(current)

                if check:
                    if lgs >= len(current):
                        continue
                    else:
                        lgs = max(lgs, len(current))
                        result = current
        return result
            
def isPalindrome(string):
    return string == string[::-1]            
