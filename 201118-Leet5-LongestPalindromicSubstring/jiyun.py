class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)
        start = end = 0
        
        if length <= 1:
            return s
        
        for i in range(length):
            max1 = self.getMax(s, i, i + 1) # even
            max2 = self.getMax(s, i, i) # odd
            maxLen = max(max1, max2)
            if maxLen >= end - start + 1:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2
        return s[start : end + 1]
            
    def getMax(self, s, left, right):
        length = len(s)
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
