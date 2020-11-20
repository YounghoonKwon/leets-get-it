class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        prefix = ''
        spot = 0
        common = True
        strs = sorted(strs, key=lambda item:len(item))
        
        while common:
            if spot >= len(strs[0]):
                break
            candidate = strs[0][spot]
            for i in range(1, len(strs)):
                if candidate != strs[i][spot]:
                    common = False
                    break
            if common:
                prefix += candidate
                
            spot += 1
        
        return prefix
