class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        if len(s) <=1 or s==s[::-1]:
            return s
        else:
            for i in range(len(s)):
                result = max(result, findSubstring(s,i,i+1), findSubstring(s,i,i+2), key=len)
            return result

def findSubstring(string, left, right):
    while left >= 0 and right <= len(string)-1 and string[left] == string[right]:
        left -=1
        right +=1
    return string[left+1:right]
