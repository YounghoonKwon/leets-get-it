import sys
class Solution:
   def romanToInt(self, s):
        rdict = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        result = 0
        prev = sys.maxsize
        for char in s:
            curr = rdict[char]
            if prev < curr:
                result = result - (prev * 2) + curr
            else:
                result += curr
            prev = curr
        return result
