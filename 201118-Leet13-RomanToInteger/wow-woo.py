class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
                  "I":1,
                  "V":5,
                  "X":10,
                  "L":50,
                  "C":100,
                  "D":500,
                  "M":1000,
                }
        #if prior number is smaller than next number, substract
        #duplicate of the same number means addiction
        result = roman[s[0]]
        pick = roman[s[0]]
        for i in range(1, len(s)):
            if pick < roman[s[i]]:
                result -= (pick*2)    
            result += roman[s[i]]
            pick = roman[s[i]]
            
        return result
