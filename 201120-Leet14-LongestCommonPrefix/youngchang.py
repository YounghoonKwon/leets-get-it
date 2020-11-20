class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs: return ""
        answer = ''
        limit = min(len(i) for i in strs)
        for i in range(limit):
            flag = False
            first = strs[0][i]
            for s in strs:
                if first != s[i]:
                    flag = True
                    break
            if flag: break
            else: answer += first
        return answer