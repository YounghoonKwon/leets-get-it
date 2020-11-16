class Solution(object):
    def romanToInt(self, s):
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        prev = 'M'
        
        for c in s:
            if d[prev] < d[c]:
                result -= 2 * d[prev]
            result += d[c]
            prev = c
        return result
