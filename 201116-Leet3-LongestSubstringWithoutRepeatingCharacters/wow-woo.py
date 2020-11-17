class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case
        if not s:
            return 0
        # careful of spaces
    
        # how many charactors
        d = {}
        left = 0
        lst = 0
        for right in range(len(s)):
            char = s[right]
            if char in d:
                if d[char] < left:
                    lst = max(lst, right-left + 1)
                else:
                    left = d[char] + 1
                d[char] = right
            else:
                d[char] = right
                lst = max(lst, right-left + 1)
        return lst
