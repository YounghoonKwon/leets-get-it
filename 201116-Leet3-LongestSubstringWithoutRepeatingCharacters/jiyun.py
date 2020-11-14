class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = {}
        start = 0
        length = 0
        for i, c in enumerate(s):
            if c in d:
                if d[c] + 1 > start:
                    start = d[c] + 1
            curLen = i - start + 1
            if curLen > length:
                length = curLen
            d[c] = i
            
        return length
