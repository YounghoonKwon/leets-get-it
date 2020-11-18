class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        shortest = min(strs, key = len)
        prefix = ''
        result = ''
        
        for c in shortest:
            prefix += c
            # if list(filter(lambda x: x.startswith(prefix), strs)) == strs:
            if all(s[:len(prefix)] == prefix for s in strs):
                result = prefix
        return result
