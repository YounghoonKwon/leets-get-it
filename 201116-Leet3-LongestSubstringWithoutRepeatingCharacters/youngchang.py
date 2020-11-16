class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        seen = set()
        answer = 0
        i = j = 0
        while j < N:
            if s[j] not in seen:
                seen.add(s[j])
                answer = max(answer, j - i + 1)
                j += 1
            else:
                seen.remove(s[i])
                i += 1
        return answer