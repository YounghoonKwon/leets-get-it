class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def sublen(s):
            out = ""
            for char in s:
                if char not in out:
                    out += char
                else:
                    return len(out)
            return len(out)
                
        maxlen = 0
        for i in range(len(s)):
            maxlen = max(sublen(s[i:]), maxlen)
        return maxlen
        
        
