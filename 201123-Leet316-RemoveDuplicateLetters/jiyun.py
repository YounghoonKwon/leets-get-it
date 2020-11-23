import collections

class Solution(object):
    def removeDuplicateLetters(self, s):
        counter = collections.Counter(s)
        stack = []
        
        for c in s:
            counter[c] -= 1
            if c in stack:
                continue
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(c)
        return ''.join(stack)
