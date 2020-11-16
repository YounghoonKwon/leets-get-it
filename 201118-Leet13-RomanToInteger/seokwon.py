import sys
class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        prev = 'M'
        for curr in s:
            if romanNum[curr] <= romanNum[prev]:
                result += romanNum[curr]
            else:
                result = result - (romanNum[prev]*2) + romanNum[curr]
            prev = curr
        return result
