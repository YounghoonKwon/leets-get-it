class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        
        n = len(strs[0])
        count = 1
        while n > 0:
            for i in range(1,len(strs)):
                sub = strs[0][:n] 
                if sub in strs[i]:
                    start_index = strs[i].index(sub)
                    if start_index == 0:
                        count +=1
            if count == len(strs):
                return strs[0][:n] 
            n -=1
            count = 1
        return ""
