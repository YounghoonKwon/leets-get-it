class Solution:
    def intToRoman(self, num: int) -> str:
        v = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4]
        s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV"]
        result = ""
        for i in range(len(v)):
            q,  r = divmod(num, v[i])
            if q > 0:
                result += q * s[i]
                num = r
                
        if num > 0:
            result += num * "I"
        return result
